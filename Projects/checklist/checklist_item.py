import datetime
import json

class CheckListItem:
    id: int = 0
    description: str = None
    status: bool = False
    somelist: list[str] = []
    somedict: dict = {}
    #created_date: datetime = None
    #completed_date: datetime = None

    def __init__(this, id, description):
        this.id = id
        this.description = description
        this.status = False
        this.somelist.append("test 1")
        this.somelist.append("test 2")
        this.somelist.append("test 3")

        this.somedict[1] = "help"
        this.somedict[2] = "help me"
        this.somedict[3] = "help him"
        #this.created_date = datetime.date.today()\
    
    def serialize(this):
        return {
            "id" : this.id,
            "description" : this.description,
            "status" : this.status,
            "list" : this.somelist,
            "dict" : this.somedict
        }

items = []
item = CheckListItem(1, "Wash the dishes")
items.append(item)
item2 = CheckListItem(2, "Do your laundry")
items.append(item2)

print(item.id, item.description)
#print(json.dumps(item.serialize()))
print(json.dumps([item.serialize() for item in items]))