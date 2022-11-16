# Objects / Classes
class PersonA:
    age = 41
    name = "Leonard"
    height = 68
    lastName = "Aguillon"

person = PersonA()
print(person.name, person.lastName)

class Person:
    def __init__(self, age, name, height, lastName):
        self.age = age
        self.name = name
        self.height = height
        self.lastName = lastName

person1 = Person(41, "Leonard", 68, "Aguillon")
if (person1.age > 21):
    print(person1.name, "is old enough to drink")

person2 = Person(33, "Olivia", 60, "Aguillon")

class Bills:
    # __init__ is our class constructor
    # when data is passed to it, it assigns the given data to the associated properties of our class
    def __init__(self, rent, electric, water, gas, phone):
        self.rent = rent
        self.electric = electric
        self.water = water
        self.gas = gas
        self.phone = phone

    # Here we are defining a function inside our class
    def total(self):
        return(self.rent + self.electric + self.water + self.gas + self.phone)

    # Here we are calling a function from another function from within the class
    def yearlyTotal(self):
        return self.total() * 12

leoBills = Bills(1350, 250, 100, 0, 115)
leosTotal = leoBills.total()
print(leosTotal)
print(leoBills.yearlyTotal())

class Pizza:
    def __init__(this, size, crust, toppings):
        this.Size = size
        this.Crust = crust
        this.Toppings = toppings

pizza = Pizza("Large", "Stuffed", ["pepperoni","jalapeno"])
print(pizza.Toppings)

# Files - Saving, reading, writing data
# File open command - uses the current directory where the script is being run FROM
# File open and reading
file = open("C:\coding\python\README.md", "r")
print(file.read())
file.seek(0, 0)
print(file.read(4))
# Read line looks for a line terminator or end of line characters like 'enter'
print(file.readline())
print(file.readline())
file.close()

#File writing
f = open("test.txt", "w")  # w is "Write" mode and will overwrite the file contents
f.write("omg i created a file!\n")
f.close()

f = open("test.txt", "a") # a is append mode and will add data to a file
f.write("hey, look another line\n")
f.write("adding another one!\n")
f.close()

# File check if file exists
def fileExists(filename):
    try:
        f = open(filename, "r")
        f.close()
        return True
    except:
        return False

print("Enter Filename:")
filename = input()

if fileExists(filename) == True:
    print("File exists, what would you like to add")
    userText = input()
    f = open(filename, "a")
    f.write(userText + "\n")
    f.close()
else:
    print("Creating new file, Add some text:")
    userText = input()
    f = open(filename, "w")
    f.write(userText + "\n")
    f.close()

f = open(filename, 'r')
f.read()
f.close()