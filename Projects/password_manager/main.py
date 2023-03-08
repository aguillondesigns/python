'''
Password manager
- Privacy: make sure no one can read the file
- Password Database
    - name
    - location
    - Credential Object
        - name (yahoo, google, )
        - username (email)
        - password
        - url
        - notes
            - mother maiden name / ...
- Functionality
    - Create a new password database
    - Check for in use passwords
    - Check password strength
        - Requirements: length, sybmols, repeated characters... 
    - Create
    - Edit/Update
    - Delete
    - Search
    - Login
        - Use hidden username/password


Decide what the basic class is going to look like
Login
Encryption - at the end
'''
import password_database as pwdb
import credential_set as cs
import time
import os
import getpass
clear = lambda: os.system('cls')

menu = {
    1 : "Create a new database",
    2 : "Login to current database",
    3 : "Exit"
}

db_menu = {
    1 : "Add new entry",
    2 : "Edit an entry",
    3 : "Delete an entry",
    4 : "Return to main menu"
}

current_database: pwdb.PasswordDatabase = None

def db_menu_loop(db):
    db_choice = 0
    while db_choice != '4':
        clear()
        for menuitem in db_menu:
            print(f"{menuitem}. {db_menu[menuitem]}")
        db_choice = input("Choose an option or search by title: ")
        handle_db_choice(db_choice, db)

def handle_db_choice(choice: str, database: str):
    global current_database
    password_db = current_database
    #password_db.title = database
    #password_db.update_credential_list()

    if choice == "1":
        credential_set = cs.CredentialSet.create()
        password_db.add_credential_set(credential_set)
        password_db.update_credential_list()

    if choice == "2":
        id = input("Enter the id of the entry to edit: ")
        credential_set = password_db.get_credential_set(id)
        updated_set = credential_set.edit()
        password_db.update_credential_set(updated_set)
        password_db.update_credential_list()

    if choice == "3":
        id = input("Enter the id of the entry to delete: ")
        password_db.delete(id)
        password_db.update_credential_list()

    if choice == "4":
        show_message("Returning to main menu...")

    if choice.isnumeric() == False:
        entries = password_db.find(choice)
        clear()
        for entry in entries:
            print(entry.id, entry.as_csv())
        pause()

def show_message(message: str):
    print(message)
    time.sleep(1)

def pause():
    print()
    input("Press enter to continue...")

def handle_choice(choice):
    global current_database
    if choice == "1":
        password_db = pwdb.PasswordDatabase()
        response = password_db.create_database()
        if response == None:
            # at this point, a new db should be created, start db specific loop
            current_database = password_db
            show_message("Database created")
            db_menu_loop(password_db.title)
        else:
            show_message(response)

    if choice == "2":
        db = input("Database Name: ")
        password_db = pwdb.PasswordDatabase()
        db_row = password_db.get_db_row(db)
        if db_row is None:
            show_message("database does not exist!")
        else:
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            hashed_password = password_db.get_hashed_password(password)
            if username == db_row[0] and hashed_password == db_row[1]:
                password_db.password = password
                password_db.salt = db_row[2]
                password_db.title = db
                current_database = password_db
                show_message("logged in!")
                db_menu_loop(db)
            else:
                show_message("invalid credentials, please try again")

    if choice == "3":
        show_message("Goodbye!")

choice = "0"
while choice != "3":
    clear()
    for menuitem in menu:
        print(f"{menuitem}. {menu[menuitem]}")
    choice = input("What would you like to do: ")
    handle_choice(choice)



# Might be a good idea to make a menu class, so we can keep the functionality simple
# and DRY (Dont Repeat Yourself)