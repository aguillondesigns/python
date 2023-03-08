class CredentialSet:
    id: str = None
    title: str = None
    username: str = None
    password: str = None
    url: str = None
    notes: str = None

    def __init__(this, title: str, username: str, password: str, url: str = "", notes: str = ""):
        this.title = title
        this.username = username
        this.password = password
        this.url = url
        this.notes = notes

    def create():
        title = CredentialSet.__get_input("Name for this credential set: ", True)
        username = CredentialSet.__get_input("Username: ", True)
        # Need to hide and verify the password
        password = CredentialSet.__get_input("Password: ", True)
        url = CredentialSet.__get_input("Website (optional): ", False)
        notes = CredentialSet.__get_input("Notes (optional): ", False)

        return CredentialSet(title, username, password, url, notes)

    def edit(this):
        print("Provide an update value or press enter to keep the old one.")
        title = this.__get_updated_input(f"Updated Title [{this.title}]: ", this.title)
        username = this.__get_updated_input(f"Updated Username [{this.username}]: ", this.username)
        password = this.__get_updated_input(f"Updated Password [{this.password}]: ", this.password)
        url = this.__get_updated_input(f"Updated Url [{this.url}]: ", this.url)
        notes = this.__get_updated_input(f"Updated Notes [{this.notes}]: ", this.notes)

        # Update the object
        this.title = title
        this.username = username
        this.password = password
        this.url = url
        this.notes = notes

        return this


    def __get_updated_input(this, question: str, original_value):
        response = input(question)
        if response == "":
            return original_value
        return response

    def __get_input(question: str, required: bool):
        response = input(question)
        if required:
            while response == "":
                response = input(question)
        return response

    def as_csv(this):
        return f"{this.title},{this.username},{this.password},{this.url},{this.notes}"


