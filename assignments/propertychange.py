# Assignment
# Display 3 Properties
# Allow the user to change one of the properties using the key
# System will generate a random property and display all 3 properties again

'''  Initial properties will be randomly generated
1 Strength 210
2 Armor 156
3 Resistance 95

Which property would you like to change? 
1

1 Life Steal 5%
2 Armor 156
3 Resistance 95

Loop until user is happy
'''

'''
Git commands to save files
1. Make sure you are in the root python folder
2. git status - tell us about any changes in our directory
3. git add [file] - add file to our list of items to be committed
4. git status - should show all our changes in green
5. git commit -m "message for commit"
6. git push - sends the data to the remote repository
'''

from random import choice, randint

# Variables dealing with armor pieces
armorPieces = ['Head', 'Shoulders', 'Chest', 'Belt', 'Legs', 'Hands', 'Feet']
selectedArmor = []
armorAsDictionary = {}

# Variables dealing with 
propertyList = ['Armor', 'Strength', 'Vitality', 'Resistance', 'Life Steal', 'Damage']
selectedProperties = []
propertiesAsDictionary = {}
propertiesWithValue = {}

percentageBased = ['Life Steal', 'Damage']
statBased = ['Armor', 'Strength', 'Vitality', 'Resistance']

def setInitialArmorPieces():
    while len(selectedArmor) < 5:
        newProperty = choice(armorPieces)
        if newProperty not in selectedArmor:
            selectedArmor.append(newProperty)

# Function to pick the initial 3 random properties
def setInitialProperties():
    while len(selectedProperties) < 3:
        newProperty = choice(propertyList)
        if newProperty not in selectedProperties:
            selectedProperties.append(newProperty)
            propertiesWithValue[newProperty] = GetRandomValue(newProperty)
        #else:
            #print(newProperty, 'already used')

def GetRandomValue(property):
    if (property in percentageBased):
        return str(randint(3, 10)) + '%'
    if (property in statBased):
        return randint(50, 200)

def GetRandomProperty():
    print("hello")

# Function to convert the selected properties to a dictionary
def convertToDictionary(list, dictionary):
    id = 1
    for property in list:
        dictionary[id] = property
        id += 1

def displayDictionaryItems(dictionary):
    for item in dictionary:
        # Print item id and the description
        print(item, dictionary[item], propertiesWithValue[dictionary[item]])

# Set the starting properties we will let the user see
setInitialProperties()
#setInitialArmorPieces()
convertToDictionary(selectedProperties, propertiesAsDictionary)
#convertToDictionary(selectedArmor, armorAsDictionary)

displayDictionaryItems(propertiesAsDictionary)

userChoice = 0
choiceInt = 0

while choiceInt not in propertiesAsDictionary:
    print("Select an item to modify (1, 2 or 3)")
    userChoice = input()
    try:
        choiceInt = int(userChoice)
    except:
        print("Invalid choice, try again")
        choiceInt = 0

propertyToChange = propertiesAsDictionary[choiceInt]
selectedProperties.remove(propertyToChange)
del(propertiesAsDictionary[choiceInt])
setInitialProperties()
convertToDictionary(selectedProperties, propertiesAsDictionary)
displayDictionaryItems(propertiesAsDictionary)
