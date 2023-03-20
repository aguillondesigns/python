import json

class Address:
    address = ''
    city = ''
    state = ''
    zip = ''
    def __init__(this, address, city, state, zip):
        this.address = address
        this.city = city
        this.state = state
        this.zip = zip

    def serialize(this):
        return json.dumps(this, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
class Pet:
    name: str = None
    age: int = 0

    def __init__(this, name, age):
        this.name = name
        this.age = age

class Person:
    name = None
    age = 0
    address: Address = None
    pets: list[str] = []

    def __init__(this, name, age, address: Address, pets: list[Pet] = []):
        this.name = name
        this.age = age
        this.address = address
        this.pets = pets

    def serialize(this):
        return {
            "name" : this.name,
            "age" : this.age,
            "address" : this.address.serialize(),
            "pets" : this.pets
        }
        # return json.dumps(this, default=lambda o: o.__dict__, 
        #     sort_keys=True, indent=4)



person = Person(
    "john", 
    27, 
    Address("123 happy lane", "san antonio", "tx", "78232"),
    [
        Pet("Roxy", 4),
        Pet("Joy", 3)
    ])
print(person.serialize())
    


