class Bills:
    def __init__(this, name, phone, house, electric, water, food):
        this.name = name
        this.phone = phone
        this.house = house
        this.electric = electric
        this.water = water
        this.food = food

    def total(this):
        return this.phone + this.house + this.electric + this.water + this.food