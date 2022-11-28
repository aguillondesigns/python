# 1. Allow user to pick the file name
# 2. Check if the file exists, add to it, if it doesnt, create it
# 3. Use a loop and write some numbers to the file
# 4. Add extras if you like!

# library imports
import functions as fun # Here I am importing my own library file

# Setup our clear
import os
clear = lambda: os.system('cls')

# Grabs the filename from the user with a small 3 character restriction
def getFilename():
    filename = input('Please provide a filename or type "quit":' + '\n')
    if (len(filename) > 3):
        return filename
    else:
        clear()
        print("Use a filename with at least 3 characters")
        getFilename()

# Uses a loop to created a 'x' line separator
def getLoopedContent(message):
    output = ''
    for char in message:
        output += '0'
    output += '\n' # add a new line character to the end
    return output

def saveMessage(filename):
    openMethod = 'w'
    if (fun.fileExists(filename)):
        message = input("Found it! What would you like to append?" + '\n')
        openMethod = 'a'
    else:
        message = input("New file eh? What would you like to add?" + '\n')
        openMethod = 'w'
    f = open(filename, openMethod)
    loopedContent = getLoopedContent(message)
    f.write(loopedContent)
    f.write(message + '\n')
    f.close()

def start():
    clear() # Clear the screen
    fun.setCurrentDirectory() # Have python switch to the current directory
    filename = getFilename()# Get a file name from the user
    if filename == 'quit':
        quit("Returning you to your regular scheduled programming")
    saveMessage(filename) # Get and save the message to the file
    fun.printFileContents(filename)
    
    


    

    




# Run the program
start()



