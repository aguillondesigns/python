import credential_set as cs
from hash import Hash
from encrypt import Encrypt
import getpass

class PasswordDatabase:
    DATASTORE = "data.pwdb"
    FILE_EXTENSION = ".db"
    HASH = "FE3BFG512851"
    title: str = None
    salt: str = None
    password: str = None
    #location: str = None
    credential_sets: list[cs.CredentialSet] = []

    def __init__(this):
        this.title: str = None
        #location: str = None
        this.credential_sets: list[cs.CredentialSet] = []

    def pause():
        input("press any key to continue")

    def get_db_row(this, title):
        this.ensure_db_exists()
        f = open(this.DATASTORE, 'r')
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.strip()
            pieces = line.split(',')
            stored_title = pieces[3]
            if title == stored_title:
                stored_user = pieces[0]
                stored_pass = pieces[1]
                stored_salt = pieces[2]
                return (stored_user,stored_pass, stored_salt)
        return None

    def get_filename(this):
        return f"{this.title}{this.FILE_EXTENSION}"

    def add_credential_set(this, credential_set: cs.CredentialSet):
        f = open(this.get_filename(), "a")
        f.write(f"{this.get_encrypted_data(credential_set.as_csv())}\n")
        f.close()

    def get_encrypted_data(this, data):
        encrypt = Encrypt(this.password, this.salt)
        return encrypt.encrypt(data).decode()

    def get_decrypted_data(this, data):
        encrypt = Encrypt(this.password, this.salt)
        return encrypt.decrypt(data)

    def delete(this, id):
        credential_sets = []
        for credential_set in this.credential_sets:
            if id == credential_set.id:
                continue
            else:
                credential_sets.append(credential_set)
        this.__clear_database()
        f = open(this.get_filename(), "a")
        for set in credential_sets:
            f.write(f"{this.get_encrypted_data(set.as_csv())}\n")
        f.close()
        
    def __clear_database(this):
        f = open(this.get_filename(), "w")
        f.close()

    def find(this, search: str):
        if len(this.credential_sets) <= 0:
            this.update_credential_list()
        results = []
        for credential_set in this.credential_sets:
            if search.lower() in credential_set.title.lower():
                results.append(credential_set)
        return results

    def get_credential_set(this, id: str):
        for credential_set in this.credential_sets:
            if id == credential_set.id:
                return credential_set

    def update_credential_list(this):
        f = open(this.get_filename(), "r")
        lines = f.readlines()
        f.close()
        sets = []
        id = 0
        for line in lines:
            if len(line) > 0:
                line = this.get_decrypted_data(line)
                id += 1
                pieces = line.strip().split(',')
                creds = cs.CredentialSet(pieces[0], pieces[1], pieces[2], pieces[3], pieces[4])
                creds.id = str(id)
                sets.append(creds)
        this.credential_sets = sets

    def update_credential_set(this, set: cs.CredentialSet):
        credential_sets = []

        # Loop through all loaded credential sets
        for credential_set in this.credential_sets:
            # if we have a id match with the update set, add the updated set instead of the original
            if set.id == credential_set.id:
                credential_sets.append(set)
            # otherwise add the original
            else:
                credential_sets.append(credential_set)

        this.__clear_database()
        f = open(this.get_filename(), "a")
        for set in credential_sets:
            f.write(f"{this.get_encrypted_data(set.as_csv())}\n")
        f.close()

    def get_hashed_password(this, password: str):
        return Hash.hash(password, this.HASH)

    def create_database(this):
        print("Creating a new password database...")
        # ask for title of the database
        title = ""
        while title == "":
            title = this.__get_unique_database_name()

        # Set the title (database name)
        this.title = title
        # Probably need to make sure the title is unique
        print("Let's set the username for your new database...")
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        this.salt = Encrypt.generate_salt()
        verify = getpass.getpass("Verify password: ")
        if verify == password:
            hashed_password = this.get_hashed_password(password)
            this.password = password
            
            # Create an association 
            f = open(this.DATASTORE, 'a')
            f.write(f"{username},{hashed_password},{this.salt},{title}\n")
            f.close()

            # Ok, lets actually create the database now
            f = open(f"{title}.db", "w")
            f.close()
            return None
        else:
            return "Password did not match!"

    def __get_unique_database_name(this):
        # Ensure the db file exists
        this.ensure_db_exists()
        title = input("Name of the new database: ")
        f = open(this.DATASTORE, 'r')
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            pieces = line.split(',')
            stored_title = pieces[3]
            if title.lower() == stored_title.lower():
                input("Invalid database name provided. Press enter to continue...")
                return ""
        f.close()
        return title
    
    def ensure_db_exists(this):
        try:
            f = open(this.DATASTORE, 'r')
            lines = f.readlines()
            f.close()
        except:
            f = open(this.DATASTORE, 'w')
            f.close()







