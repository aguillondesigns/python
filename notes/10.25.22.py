# How do call for a function to be used
#print("a string")
'''
def print2(words = 'no words '):
    print(words * 2)

print2("big words ")

list = []
'''

# ask user for their email or phone number
# Keep grocery list from user
# make sure i have an empty list
# use a while loop to keep collecting groceries
# ask user if they are done to exit loop, maybe look for a keyword in the input to stop the loop
# print full list when they are done
# save it to a file, send a text message, send an email...

# while their answer is yes:
    # ask for another item
def getGroceryItem ():
    print("What do you want to add to your list?")
    item = input()
    return item

groceryList = []

answer = "intial"

while len(answer) > 0:
    print("Type in a new item to add it to the list or press enter to quit")
    answer = getGroceryItem()
    if answer != '':
        groceryList.append(answer)

print(groceryList)


