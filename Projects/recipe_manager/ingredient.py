class Ingredient:
    name: str = None
    quantity: str = None
    measurement: str = None

    def __init__(this, name, quantity, measurement):
        this.name = name
        this.quantity = quantity
        this.measurement = measurement

    def serialize(this):
        return {
            "name" : this.name,
            "quantity" : this.quantity,
            "measurement" : this.measurement
        }
