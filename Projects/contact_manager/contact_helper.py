from address import Address
from contact import Contact

class ContactHelper:

    contacts: list = []

    def __init__(this, file):
        this.contacts = []
        this.__load_contacts(file)

    def __load_contacts(this, file):
        # Grab the number of lines
        f = open(file, 'r')
        numberLines = len(f.readlines())
        f.seek(0, 0)    # Reset our file position
        line = 0
        while line < numberLines:
            currentLine = this.sanitize(f.readline())
            pieces = this.get_sanitized_pieces(currentLine)
            address = Address(pieces[2],pieces[3],pieces[4],pieces[5])
            contact = Contact(pieces[0], pieces[1], address, pieces[6], pieces[7])
            contact.id = str(line + 1)
            this.contacts.append(contact)
            line += 1

    def find_contact(this, file, search):
        this.contacts = []
        this.__load_contacts(file)
        hasSearch = []
        for contact in this.contacts:
            if search in contact.first_name:
                hasSearch.append(contact)
        return hasSearch

    def get_contact(this, file, id):
        this.contacts = []
        this.__load_contacts(file)
        for contact in this.contacts:
            if contact.id == id:
                return contact

    def update_contact(this, file, id, updated_contact):
        this.contacts = []
        this.__load_contacts(file)
        f = open(file, 'w')
        for contact in this.contacts:
            if contact.id == id:
                f.write(updated_contact.as_csv() + "\n")
            else:
                f.write(contact.as_csv() + "\n")
        f.close()
                
    def delete_contact(this, file, id):
        f = open(file, 'w')
        foundContact = False
        for contact in this.contacts:
            if contact.id == id:
                foundContact = True
            else:
                f.write(contact.as_csv() + "\n")
        f.close()
        return foundContact

    def get_count(this):
        return len(this.contacts) + 1

    def sanitize(this, item):
        return str(item).strip()

    def get_sanitized_pieces(this, line):
        pieces = str(line).split(',')
        cleaned = []
        for piece in pieces:
            cleaned.append(this.sanitize(piece))
        return cleaned