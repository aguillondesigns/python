# Homework
''' Using the login above, use a while loop
to make the system keep asking for a username until
the user provides a username from your list

if user gives right username, say something like
Login Successfull
if user gives wrong username, say something like
Login Failed, Ask for the username again

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

loggedIn = False
while loggedIn == False:
    user = login()
    validUser = checkUser(user)
    if validUser:
        loggedIn = True
        print("Login Successfull. Welcome " + getUser(user))
    else:
        print("Login Failed.")

