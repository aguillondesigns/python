import menu
from ingredient import Ingredient
from recipe import Recipe
from search_index import Index, SearchIndex
import os
clear = lambda: os.system('cls')


class RecipeManager:
    main_menu_options = ["Add new recipe", "List all recipes","Scan for new recipes"]
    edit_menu_options = ["Modify existing recipe", 
                         "Delete a recipe", 
                         "Start making a recipe"]
    main_menu: menu.Menu = None
    search_index: SearchIndex = None
    system_message = ""

    def __init__(this):
        main_menu = menu.Menu()
        main_menu.set_options(this.main_menu_options)
        this.main_menu = main_menu
        this.search_index = SearchIndex()

    def run(this):
        while True:
            # Draw menu
            this.__draw_menu()

            # Handle menu response
            this.__handle_menu_response()

    def __draw_menu(this):
        clear()
        if this.system_message != "":
            print(this.system_message)
            print()
            this.system_message = ""
        options = this.main_menu.get_options()
        for menu_item in options:
            print(menu_item, options[menu_item])

    def convert_recipe_path(this, name: str):
        # Index example: chili cheese hot dogs
        # File example: recipes/chili_cheese_hot_dogs.json
        name = name.replace(' ', '_')
        return f"recipes/{name}.json"

    def __handle_edit_menu_response(this, choice):
        # Edit a recpipe
        if choice == '1':
            input("Edit recipe... press enter to continue")

        # Delete a recipe
        if choice == '2':
            id = input("Which recipe id would you like to delete? ")
            # Confirm deletion
            recipe_index = this.search_index.get_recipe_by_id(id)
            confirm = input("Are you sure you want to delete " + 
                f"{recipe_index.recipe_name} (y/n)? ")
            if confirm == "y":
                # Need to delete the recipe that has the id that matches what they picked
                recipe_path = this.convert_recipe_path(recipe_index.recipe_name)
                if os.path.exists(recipe_path):
                    os.remove(recipe_path)
                else: 
                    print(f"{recipe_path} does not exist!")

                # Need to delete the recipe the search index
                # Need to refresh the in memory data
                # Reload the list with the new ids
                this.search_index.delete(recipe_index.id)
                this.system_message = "Recipe deleted."
            else:
                print("No recipes were harmed during this action")
                this.pause()

        # Start making a recipe
        if choice == '3':
            # Grab id that we are making
            id = input("Which recipe id would you like to make? ")

            this.start_recipe(id)

    def start_recipe(this, id):
        # Need to get our recipe from file
        recipe = this.search_index.get_full_recipe(id)
        # Ask how many people we are feeding
        servings_wanted = input(f"How many servings of {recipe.name} would you like? ")

        clear()
            # Title
        print(f"Making: {recipe.name} for ({servings_wanted} people)")
        print()
            # Show notes
        print(f"Notes: {recipe.notes}")
        print()
            # Ingredients - Use stepping tool
        print(f"Ingredients: (Press enter to move to next ingredient)")
        print()
        for ingredient in recipe.ingredients:
            servings_per_person = this.get_servings_per_person(int(recipe.servings), float(ingredient.quantity))
            calcualted_quantity = round(servings_per_person * int(servings_wanted),2)
            print(f"{calcualted_quantity} {ingredient.measurement} of {ingredient.name}")
            input()
        
        print()
            # Steps - Use stepping tool
        print(f"Steps: (Press enter to move to next step)")
        print()
        for step in recipe.steps:
            print(step)
            input()

        print()
        input("Recipe complete! press enter to return to the main menu")

    def get_servings_per_person(this, servings, quantity):
        return quantity / servings

    def calculate_quantity(this, servings, measurement):
        # For now, dirty math
        # Fix this up later so it can return even number, possibly fractions
        return servings * measurement

    def __handle_menu_response(this):
        choice = input("Type to search or pick an option? ")
        # Add a recipe
        if choice == '1':
            recipe_name = input("Name of the recipe: ")
            number_servings = input("Number of servings: ")
            ingredient_list = []
            
            # Get the first ingredient from the user
            ingredient_name = input("Ingredient name: ") # milk
            ingredient_quantity = input("Quantity: ") # 1
            ingredient_measurement = input("Measurement: ") # cup
            
            # Convert those pieces to an ingredient object
            ingredient = Ingredient(ingredient_name, ingredient_quantity, ingredient_measurement)

            # Saving our ingredient to the ingredients list
            ingredient_list.append(ingredient)

            while ingredient != None:
                ingredient = this.__get_ingredient()
                if ingredient != None:
                    ingredient_list.append(ingredient)

            # Add recipe steps
            recipe_steps = []

            step = input(f"Step {len(recipe_steps) + 1}: ") # need to make sure this is not empty
            recipe_steps.append(step)

            while step != '':
                step = input(f"Step {len(recipe_steps) + 1}: ")
                if step != '':
                    recipe_steps.append(step)

            # categories
            categories = input("Categories (comma separated: chinese, rice, chicken...): ")
            # need to convert the comma separated values into a list of strings

            # notes
            notes = input("Any notes: ")

            recipe = Recipe(recipe_name, number_servings, ingredient_list, recipe_steps, categories, notes)
            recipe.save()

            # Need to update our search index
            index = Index(recipe.name, recipe.categories)
            this.search_index.save(index)
        
        # List all recipes
        if choice == '2' or choice == '':
            clear()
            all_recipes = this.search_index.get_all_recipes()
            for recipe in all_recipes:
                print(f"{recipe.id}. {this.format_name(recipe.recipe_name)}")
            this.pause()

        # Scan recipes folder for new recipes
        if choice == '3':
            recipe = Recipe()
            # Get the directory that is holding all the recipes
            recipe_path = recipe.create_recipe_directory()
            # Here we are clearing out the 'in memory' recipes
            this.search_index.index = []
            # Loop through all files in the folder (they should all be recipes)
            for filename in os.listdir(recipe_path):
                f = os.path.join(recipe_path, filename)
                # checking if it is a file
                if os.path.isfile(f):
                    # french_toast.json -> french toast
                    filename = filename.replace('_', " ").replace(".json", "")

                    # Load each file as a recipe object
                    new_recipe = Recipe(filename)
                    new_recipe.load()

                    # Write all of the new data to the search.index
                    # Need to update our search index
                    index = Index(new_recipe.name, new_recipe.categories)
                    this.search_index.save(index)
            this.system_message = "Recipes updated!"

        # Exit program
        if choice == '4':
            clear()
            exit("Thanks for using Recipe Manager! Ciao")

        # Here we are handling the searching 
        if choice.isnumeric() == False and choice != '':
            clear()
            matches = this.search_index.get_recipes(choice.lower())
            if len(matches) > 0:
                for recipe in matches:
                    print(f"{recipe.id}. {this.format_name(recipe.recipe_name)}")
                # Since we have a match, give them options to edit, delete or start
                edit_menu = menu.Menu()
                edit_menu.set_options(this.edit_menu_options, "Return to main menu")
                this.draw_edit_menu(edit_menu)
                
            else:
                print("No recipes found with that name or category")
                #input("Would you like to add a new recipe?")
                # Since we did not find a match, guide them to the add a recipe
                this.pause()

    def draw_edit_menu(this, edit_menu: menu.Menu):
        print()
        options = edit_menu.get_options()
        for menu_item in options:
            print(menu_item, options[menu_item])
        choice = input("Pick an option or hit enter to go to the main menu: ")
        # handle the choice, then let user go back to regular menu
        this.__handle_edit_menu_response(choice)
        # if they do not choose anything, send them to main menu

    def format_name(this, string):
        words = string.split(" ")
        updated_words = []
        for word in words:
            updated_words.append(word.capitalize())
        return " ".join(updated_words)

    def pause(this):
        input("Press enter to continue...")

    def __get_ingredient(this):
        # Get the first ingredient from the user
        ingredient_name = input("Ingredient name: ") # milk
        if ingredient_name == "":
            return None
        ingredient_quantity = input("Quantity: ") # 1
        ingredient_measurement = input("Measurement: ") # cup
        
        # Convert those pieces to an ingredient object
        ingredient = Ingredient(ingredient_name, ingredient_quantity, ingredient_measurement)

        return ingredient

rm = RecipeManager()
rm.run()