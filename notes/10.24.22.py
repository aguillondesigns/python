# boolean values
evenNumberList = ["0", "2", "4", "6", "8"]
myNumber = 226

def modIsEven(num):
    modValue = num % 2
    if modValue > 0:
        return False
    return True

def isEven(num):
    mynum = str(num)
    #print(mynum[-1])
    lastDigit = mynum[-1]
    if lastDigit in evenNumberList:
        return True
    return False

print(modIsEven(myNumber))
print(isEven(myNumber))

from random import randint

name = "isa"
while (name != "munch") and (name != "isa"):
    print("Your not one of my children!")

# if statements
age = 14

if age < 21:  # age < 21, age > 21, age != 18, age == 18, age <=.., >=... age in [list]  
    cantSmoke = True
elif age < 65:
    cantSmoke = False
else:
    cantSmoke = True

# random number functions
messages = { 1 : "Not Today", 2 : "Try again later", 3 : "Definitely Not!", 4 : "There's a chance", 5 : "Yes" }

print("What's your question?")
question = input()
randomNumber = randint(1,5)
#print(randomNumber)
print(messages[randomNumber])


def getNumbers(numbers):
    numbersToReturn = []
    i = 0
    while i < numbers: 
        numbersToReturn.append(randint(1, 65))
        i = i + 1  # shorthand version: i += 1
    return numbersToReturn

def playPowerball():
    print("Here are you lucky numbers:")
    numbers = getNumbers(5)
    print(numbers)

playPowerball()







