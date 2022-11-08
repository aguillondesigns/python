#users = { "Leo" : "Leonard Aguillon", "Bolis" : "Olivia Aguillon", "Bee" : "Livier Aguillon"}
'''
tempname = "" # global string

def greetUser (username):
    fullname = users[username]
    #print(fullname)
    global tempname # using global string
    tempname = fullname
    return fullname

# for some reason, we have the user name, maybe they logged in?
name = greetUser("Bolis")
#print ("Welcome " + name + "!")

print(tempname)

# do function with optional parameter/argument
def optional (firstName, lastName = ""):
    print("Hello " + firstName + " " + lastName)
    return

optional("John", "Doe")
optional("Mark")


# Take in data

print("Enter the password")
password = input()
print("Password: " + password)
'''

users = { "Leo" : "Leonard Aguillon", "Bolis" : "Olivia Aguillon", "Bee" : "Livier Aguillon"}

def checkUser (username):
    if username in users:
        return True
    else:
        return False

def getUser (username):
    fullname = users[username]
    return fullname

def login ():
    print("Enter your user name:")
    username = input()
    return username

user = login()
validUser = checkUser(user)
if validUser == True:
    print("Hello " + getUser(user))






