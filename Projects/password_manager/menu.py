class Menu:
    menu_options: dict = {}

    def __init__(this):
        this.menu_options = {}

    def set_options(this, options: list):
        i = 0
        for option in options:
            i += 1
            this.menu_options[i] = option

    def get_options(this):
        updated_menu = this.menu_options
        updated_menu[len(this.menu_options) + 1] = "Exit"
        return updated_menu


'''
menu = Menu()

menu.set_options(['Menu Option 1', 'Menu Option 2', 'Menu Option 3'])
print(menu.get_options())
'''