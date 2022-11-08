
# Homework
# Bonus item - keep the screen clean (google)
# Require proper login, 3 attempts - if failed 3 times, exit app with a message like 'Unable to login at this time'
# Receipt calculator - Ask the for the amounts, Take in x amount of receipts
# Print reciepts taken in: line by line, sort list by least expensive to most expensive, $xx.xx
# When done, diplay the rounded the total, $xxxx
# 
# Todo/Chore List
# 

import os
import locale
locale.setlocale(locale.LC_ALL, '')
clear = lambda: os.system('cls')

users = { "Leo" : "Leonard Aguillon", "Bee" : "Livier Aguillon", "Munch" : "Leonardo Aguillon", "Chavez" : "Isabel Aguillon" }

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

# Handle the login logic
loggedInUser = ''
loginAttempts = 0
def doLogin():
    # Clear the screen
    clear()
    global loggedInUser
    loggedIn = False
    while loggedIn == False:
        global loginAttempts
        if loginAttempts >= 3:
            exit("Too many login attempts, Exiting...")
        loginAttempts += 1
        user = login()
        validUser = checkUser(user)
        if validUser:
            clear()
            loggedIn = True
            print("Login Successfull. Welcome " + getUser(user))
            loggedInUser = user
        else:
            print("Login Failed.")

# Handle the receipt collection
receipts = []

# Format a value to currency format
def getFormattedValue(value):
    return locale.currency(value, grouping=True)

# Returns the total of our receipts
def getTotal():
    total = 0.0
    for receipt in receipts:
        total += receipt
    return round(total, 0)

# Draws out each receipt in money format
def showReceipts():
    if len(receipts) > 0:
        print("Receipts Entered:")
        for receipt in receipts:
            print(locale.currency(receipt))

# Here is where we do our loop to get the receipts 
def getReceipts():
    receipt = 0.0
    while receipt != '':
        clear()
        showReceipts()
        print("Enter the receipt amount or hit enter to finish")
        receipt = input()
        if receipt != '':
            try:
                receiptAsFloat = float(receipt)
                receipts.append(receiptAsFloat)
            except:
                print("Are you sure you typed '", receipt, "' correctly?")
        else:
            clear()
            showSummary()

# Draws out the final page of our application
def showSummary():
    clear()
    print("Thanks " + getUser(loggedInUser))
    print("Your receipt total is: " + str(locale.currency(getTotal())))
    showReceipts()


# Her we are actually running the functions
doLogin()
getReceipts()