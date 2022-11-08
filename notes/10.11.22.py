# accessing strings
mystring = "Cheese loves to melt on the floor"
mystring = "78247-4587"
mystring = "210-744-2060"
mystring = "192.168.10.16"
print(mystring[1])  # first character
print(mystring[-1]) # last character
print(mystring[0:5]) # range of characters

# Lists
pets = ['cat','dog','fish','gerbil']
pets = [17, 'fish', "dog", 1000.00]
print(pets)
print(pets[-2])
print(pets[1:4])

# Tuple
dogs = ('german shepherd', 'golden retriever', 'boxer', 'yorkie')
#dogs[0] = 'pit bull' Throws error, tuples cannot be updated
print(dogs[0])


# Dictionary - set of key value pairs
webster = {}
webster[0] = "0value"
webster[1] = '1value'
webster['a'] = 'avalue'

#webster = {'cat':'jerk','dog':'friend','mouse':'cat food'}
print(webster)
print(webster['a'])

# Loops  For Loop, While Loop
# For Loop - do something while the condition is true, fixed number of times
pets = ['cat','dog','fish','gerbil']
for pet in pets:
    print(pet)

x = 0
i = 0
while (x < 10):
    x = x + 1
    i = x
    print(x * i)

# 10x10 Cube, any character, must loops












