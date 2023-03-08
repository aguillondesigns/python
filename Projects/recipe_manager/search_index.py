# list of all recipe names, corresponding categories

class Index:
    id: int = 0
    recipe_name: str = None
    categories: list[str] = []

    def __init__(this, name, categories, id = 0):
        this.recipe_name = name
        this.categories = categories
        this.id = id

    def to_csv(this):
        categories = ",".join(this.categories)
        return f"{this.recipe_name.lower()},{categories}"

class SearchIndex:
    index: list[Index] = []
    filename = "search.index"

    def __init__(this):
        this.__load()

    def __load(this):
        this.index = []
        # Here we need to load all the data from the search.index file
        f = open(this.filename, 'r')
        lines = f.readlines()
        f.close()
        id = 0
        for line in lines:
            id += 1
            # recipe name, category, category, category..
            pieces = line.split(',')
            recipe_name = pieces[0].strip().lower()
            categories = []
            pieces.pop(0)
            for piece in pieces:
                piece = piece.strip()
                if piece != '':
                    categories.append(piece)
            this.index.append(Index(recipe_name, categories, id))

    def show_all(this):
        for index in this.index:
            print(index.recipe_name,index.categories)

    def get_all_recipes(this):
        return this.index
    
    def get_recipe_by_id(this, id):
        for index in this.index:
            if id == str(index.id):
                return index
        return None 

    def get_recipes(this, search):
        return_data: list[Index] = []
        for index in this.index:
            if search in index.recipe_name:
                return_data.append(index)
                continue
            for category in index.categories:
                if search in category:
                    return_data.append(index)
                    break
        return return_data
            
    def save(this, new_index: Index):
        this.index.append(new_index)
        f = open(this.filename, 'w')
        for index in this.index:
            f.write(index.to_csv() + "\n")
        f.close()
        this.__load()

    def delete(this, id):
        f = open(this.filename, "w")
        for index in this.index:
            if id != index.id:
                f.write(index.to_csv() + "\n")
        f.close()
        this.__load()





