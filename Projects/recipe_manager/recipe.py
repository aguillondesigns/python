import os, json
from ingredient import Ingredient
clear = lambda: os.system('cls')


class Recipe:
    name = None
    servings: int = 0
    ingredients: list[Ingredient] = []
    steps: list[str] = []
    categories = None
    notes: str = None
    recipe_directory = "recipes"

    def __init__(this, name: str = None, servings: int = 0, 
            ingredients: list[Ingredient] = [], steps: list[str] = [], 
        categories: str = None, notes: str = None):
        this.name = name
        this.servings = servings
        this.ingredients = ingredients
        this.steps = steps
        this.categories = categories
        this.notes = notes

    # Here we are going to take a recipe name and find the recipe that its
    # associated with
    def load(this):
        recipe_directory = this.create_recipe_directory()
        # target_file looks like this: "recipes/french_toast.json"
        target_file = os.path.join(recipe_directory, this.get_filename())
        # Open, read and close the file when done
        with open(target_file) as recipe_file:
            file_contents = recipe_file.read()

        # This loads an object as a json object
        json_content = json.loads(file_contents)

        # Here we are resetting the properties of this object from the file data
        this.name = json_content["name"]
        this.servings = json_content["servings"]
        ingredients = []
        for ingredient in json_content["ingredients"]:
            ing = Ingredient(ingredient["name"], ingredient["quantity"], ingredient["measurement"])
            ingredients.append(ing)
        this.ingredients = ingredients
        this.steps = json_content["steps"]
        this.categories = json_content["categories"]
        this.notes = json_content["notes"]

    def serialize(this):
        return json.dumps(this, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

    def save(this):
        # Ensures that each data set is the way we want to store it
        this.__validate_recipe()
        # Write the file to disk
        this.__write()

    # Converts file name as such: "French Toast -> french_toast.json"
    def get_filename(this):
        return this.name.lower().replace(" ","_") + ".json"

    def __write(this):
        recipe_directory = this.create_recipe_directory()
        target_file = os.path.join(recipe_directory, this.get_filename())
        serialized_object = this.serialize()
        f = open(target_file, 'w')
        f.write(str(serialized_object))
        f.close()

    def create_recipe_directory(this):
        # first, check and see if the directory already exists
        current_directory = os.path.realpath(os.path.dirname(__file__))
        recipe_path = os.path.join(current_directory, this.recipe_directory)
        # if it does, we are done
        if os.path.exists(recipe_path):
            return recipe_path
        # if not, create it
        else:
            os.mkdir(recipe_path)
            return recipe_path

    def __validate_recipe(this):
        this.name = this.__validate_name()
        this.servings = int(this.servings) # code will break if they type in a letter
        this.ingredients = this.__validate_ingredients()
        this.steps = this.__validate_steps()
        this.categories = this.__validate_categories()

    def __validate_name(this):
        words = this.name.lower().split(" ")
        update_words = []
        for word in words:
            update_words.append(word.capitalize())
        return " ".join(update_words)

    def __validate_ingredients(this):
        temp: list[Ingredient] = []
        for ingredient in this.ingredients:
            name = ingredient.name.capitalize()
            quantity = float(ingredient.quantity)
            measurement = ingredient.measurement.lower()
            ing = Ingredient(name, quantity, measurement)
            temp.append(ing)
        return temp

    def __validate_steps(this):
        temp: list[str] = []
        for step in this.steps:
            temp.append(step.capitalize())
        return temp

    def __validate_categories(this):
        temp: list[str] = []
        categories = this.categories.split(',')
        for category in categories:
            temp_category = category.strip()
            if temp_category != '':
                temp.append(temp_category)
        return temp


# notes = "this recipe is pretty sweet, cut the powdered sugar down by half"
# categories = "french toast, french, , , cat, dog, toast, breakfast, "
# steps = ["combine dry ingredients","add in butter", "fry until gold brown"]
# ingredients = [Ingredient("whole Grain Bread", 8, "Slices"), Ingredient("milk", ".5", "cup"),
# Ingredient("cinnamon", ".5", "tbsp"), Ingredient("egg", "1", "whole")]
# recipe = Recipe("French toast", 4, ingredients, steps, categories, notes)
# recipe.save()
