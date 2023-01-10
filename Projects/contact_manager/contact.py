from address import Address

class Contact:
    id = 0
    first_name = None
    last_name = None
    address = None
    email = None
    phone = None

    def __init__(this, first_name: str, last_name: str = "", address = Address(), 
        email: str = "", phone: str = ""):

        this.first_name = first_name.strip()
        this.last_name = last_name.strip()
        this.address = address
        this.email = email.strip()
        this.phone = phone.strip()

    def __str__(this) -> str:
        return (f"{this.id}. {this.first_name} {this.last_name} - {this.phone} ({this.email}) \n" +
            "     " + this.address.as_csv())
    
    def as_csv(this):
        fields = [this.first_name, this.last_name, this.address.as_csv(), this.email, this.phone]
        return ','.join(fields)

