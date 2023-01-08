menu = {
    1 : "Add a contact",
    2 : "Edit a contact",
    3 : "Delete a contact",
    4 : "Exit"
}

def handle_choice(choice):
    if choice == '4':
        exit("Goodbye!")

    if choice == '1':
        input("add a contact...")

while True:
    for item in menu:
        print(item, menu[item])
    choice = input("What would you like to do: ")
    handle_choice(choice)