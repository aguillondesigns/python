ages = {'Leo':15, 'Livier':19, 'Bolis':10}
highScore = max(ages.values())
highUser = max(ages, key=ages.get)
print(str(highUser) + ":" + str(highScore))

from random import seed, shuffle
from secrets import choice

# Dictionary Keys/Values
dictionary = { 1 : 'a', 2 : 'b', 3 : 'c'}
list = [1, 2, 3, 9, 8, 7, 4, 5, 6, 0]

print(dictionary.keys())
for key in dictionary.keys():
    print(key)

print()

print(dictionary.values())
for value in dictionary.values():
    print(value)

# More random number functions
seed(98)
print(choice(list))
shuffle(list)
print(list)

# string methods
# capitalize, center(width, fill_character), count(str, beg=0, end=len(string))

# dates