class Menu:
    menu_options: dict = {}

    def __init__(this):
        this.menu_options = {}

    def set_options(this, options: list, exit_menu = "Exit"):
        i = 0
        for option in options:
            i += 1
            this.menu_options[i] = option
        i += 1
        this.menu_options[i] = exit_menu

    def get_options(this):
        return this.menu_options


'''
menu = Menu()

menu.set_options(['Menu Option 1', 'Menu Option 2', 'Menu Option 3'])
print(menu.get_options())
'''