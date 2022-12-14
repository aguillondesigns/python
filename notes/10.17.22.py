
# Math functions
from filecmp import cmp
from math import ceil, floor

absoluteValue = abs(-7) # distance from zero
print(absoluteValue)

ceilValue = ceil(99.02)  # ceil always goes UP
print(ceilValue)

floorValue = floor(99.99) # floor always goes down
print(floorValue)

def compareValue(a, b):
    return a == b

compareVal = compareValue('one', 'One')
print(compareVal)



# other function exp(exponent of), log(logarithm of), log10(logarithm of base 10)
# max(item1, item2), min(item1, item2), sqrt(square root), round(value, places)


people = {'Leo' : 41, 'Munch' : 15, 'Isa' : 17,  'Zebra' : 1, 'Livier' : 36, 'Donald' : 14, 'Olivia' : 33}
numbers = {27 : "R", 35 : "Z", 96 : "N", 1 : "A", 13 : "C" }
#print(sorted(people.items(), key=lambda item: item[1]))
# max() sorts by the "key" in the dictionary

print(max(people))
print(min(people))
print(max(numbers))
print(max(100,200,300,400,500))
print(min(100,200))

# Functions
def printMe (str):  # function can take in x amount of parameters
    print (str)
    return

printMe("printMe example")
printMe(people)

def multiply (intA, intB):
    answer = intA * intB
    #print(answer)
    return answer

def printCube (pattern):
    for char in pattern:
        print(pattern)
    return


printMe("Leo Rules")

x = multiply(9, 100)
y = multiply(x, 100)
z = multiply(y, x)

print(x,y,z)

printCube("!!!!!!!!!!!!!!!!!!!!!!!!!!")

