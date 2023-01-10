from contact import *
from address import *
from contact_helper import *
import os
clear = lambda: os.system('cls')

class ContactManager:
    CONTACTS = "contacts.csv"

    is_running = False
    options = {}
    action_status = ""
    current_contacts = {}
    contact_helper = None

    def __init__(this):
        this.is_running = True
        this.options = {
            1 : "Add a new contact.",
            2 : "Display current contacts.",
            3 : "Find, Edit or Delete a contact.",
            4 : "Clear my current database.",
            5 : "Exit Contact Manager"
        }
        this.action_status = ""
        this.current_contacts = {}
        this.contact_helper = ""

    def run(this):
        this.__load_contact_helper()
        while this.is_running:
            this.__gather_input()

    def __load_contact_helper(this):
        this.contact_helper = ContactHelper(this.CONTACTS)

    def __gather_input(this):
        clear()
        this.__center("Contact Manager 0.1")
        if this.action_status != '':
            print(this.action_status)
            this.action_status = ''
        message = f"Select an option below ( {min(this.options.keys())} - {max(this.options.keys())} )"
        this.__display_options(message)
        choice = input()
        this.__handle_choice(choice)

    def __display_options(this, title):
        module = __import__('text_utils')
        module.lower_text(this.options, title)

    def __center(this, text):
        module = __import__('text_utils')
        module.center_text(text)

    def __handle_choice(this, choice):
        if choice == "1": # Add new contact
            this.__add_contact()
            this.__load_contact_helper()

        if choice == "2": # Display contacts
            this.__display_contacts(None, "Current Contacts")

        if choice == "3": # Find contact
            clear()
            search = input("Enter a partial name of the person you want to find: ")
            if len(search) > 0:
                this.__load_contact_helper()
                results = this.contact_helper.find_contact(this.CONTACTS, search)
                if len(results) > 0:
                    for contact in results:
                        print(contact.__str__())
                        print()
                choice = input("Would you like to (e)dit, (d)elete, or enter to go home: ")
                this.__handle_changes(choice)

        if choice == "4": # Clear Contacts
            confirm = input("Type 'yes' to confirm: ")
            if confirm == "yes":
                with open(this.CONTACTS, 'w'):
                    clear()
                    this.action_status = "contacts cleared"
                this.__load_contact_helper()

        if choice == "5": # Exit app
            this.__exit_app()

    def __handle_changes(this, choice):
        if choice == "e":
            id = input("Enter the id of the contact: ")
            contact = this.contact_helper.get_contact(this.CONTACTS, id)
            this.__center("Editing Contact")
            print("Enter new value or press enter to keep the same")
            this.__edit_contact(contact)
            this.action_status = "contact updated."
            # do edit
        if choice == "d":
            id = input("Enter the id of the contact: ")
            removed = this.contact_helper.delete_contact(this.CONTACTS, id)
            if removed:
                this.action_status = "contact removed."
        this.__load_contact_helper()

    def __edit_contact(this, contact):
        first_name = this.__get_input(f"First Name: {contact.first_name}", contact.first_name)
        last_name = this.__get_input(f"Last Name: {contact.last_name}", contact.last_name)
        address = this.__get_input(f"Address: {contact.address.address}", contact.address.address)
        city = this.__get_input(f"City: {contact.address.city}", contact.address.city)
        state = this.__get_input(f"State: {contact.address.state}", contact.address.state)
        zip = this.__get_input(f"Zip: {contact.address.zip}", contact.address.zip)
        email = this.__get_input(f"Email: {contact.email}", contact.email)
        phone = this.__get_input(f"Phone: {contact.phone}", contact.phone)

        updated_address = Address(address, city, state, zip)
        updated_contact = Contact(first_name, last_name, updated_address, email, phone)
        updated_contact.id = contact.id
        this.contact_helper.update_contact(this.CONTACTS, updated_contact.id, updated_contact)

    def __get_input(this, message, value):
        updated_input = input(f"Current value of [{message}]: ")
        if updated_input == "":
            return value
        return updated_input

    def pause(this):
        input("Press enter to continue ...")
        
    def __add_contact(this):
        clear()
        this.__center("Add a contact")
        print("Press enter to skip any unknown fields, first name is required.")
        first_name = input("First name: ")
        last_name = input("Last name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip = input("Zip code: ")
        email = input("Email address: ")
        phone = input("Phone number (digits only): ")
        if len(first_name) > 0:
            address = Address(address, city, state, zip)
            contact = Contact(first_name, last_name, address, email, phone)
            contact.id = this.contact_helper.get_count()
            this.__save_contact(contact)
            this.action_status = "contact saved."

    def __display_contacts(this, contacts = None, title = None):
        clear()
        if title != None:
            this.__center(title)
        if contacts == None:
            contacts = this.contact_helper.contacts

        for contact in contacts:
            print(contact.__str__())
            print()
        this.pause()

    def __save_contact(this, contact):
        with open('contacts.csv', 'a') as file:
            file.write(contact.as_csv() + "\n")

    def __exit_app(this):
        clear()
        exit("Thanks for using contact manager, Goodbye!")


cm = ContactManager()
cm.run()
