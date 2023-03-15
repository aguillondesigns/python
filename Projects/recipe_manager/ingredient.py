import json


class Ingredient:
    name: str = None
    quantity: str = None
    measurement: str = None

    def __init__(this, name, quantity, measurement):
        this.name = name
        this.quantity = quantity
        this.measurement = measurement

    def serialize(this):
        return json.dumps(this, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
