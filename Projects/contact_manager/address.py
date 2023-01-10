class Address:
    address = None
    city = None
    state = None
    zip = None

    def __init__(this, address = "", city = "", state = "", zip = ""):
        this.address = address
        this.city = city
        this.state = state
        this.zip = zip

    def __str__(this) -> str:
        return f"{this.address}, {this.city}, {this.state}, {this.zip}"

    def as_csv(this):
        fields = [this.address, this.city, this.state, this.zip]
        return ','.join(fields)