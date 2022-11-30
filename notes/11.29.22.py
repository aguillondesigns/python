import os
clear = lambda: os.system('cls')

class Bills:
    def __init__(this, name, phone, house, electric, water, food):
        this.name = name
        this.phone = phone
        this.house = house
        this.electric = electric
        this.water = water
        this.food = food

    def total(this):
        return this.phone + this.house + this.electric + this.water + this.food

def saveToFile(name, total):
    filename = 'total.txt'
    f = open(filename, 'a')
    f.write(name + ": " + str(total) + "\n")
    f.close()

def clearFile():
    filename = 'total.txt'
    f = open(filename, 'w')
    f.close() 

clear()
clearFile() # using this to clear out our save file 
f = open("test.csv", "r") # our csv we are opening
numberLines = len(f.readlines()) # determine the number of lines in it
f.seek(0, 0) # reset the file pointer
startingLine = 0 # set our starting point
runningTotal = 0
recordsProcessed = 0
while startingLine < numberLines:
    line = f.readline() # reads an entire line from the file
    line = line.strip() # clean off the newline character \n
    #print(line)
    # split will split apart a string by whatever delimeter is provided
    pieces = line.split(',')
    cleanPieces = []
    for piece in pieces:
        cleanPieces.append(piece.strip())
    # Turn this into an object
    if str(cleanPieces[1]).isdigit():
        userBills = Bills(cleanPieces[0], int(cleanPieces[1]), int(cleanPieces[2]), 
        int(cleanPieces[3]), int(cleanPieces[4]), int(cleanPieces[5]))
        print(userBills.name, ": ", userBills.total())
        saveToFile(userBills.name, userBills.total())
        runningTotal += int(userBills.total())
        recordsProcessed += 1
    #else:
        #print("skipped: ", line)
    
    #print(userBills.electric)
    '''
    for piece in pieces: # looping through the split apart pieces
        piece = piece.strip() # using strip to clean off empty spaces
        print(piece)'''
    startingLine += 1

print()
print("Records Procesed: ", recordsProcessed)
print("Running Total: ", runningTotal)
'''
x 1. Read in a csv file
x 2. Process each line of the csv file
    x a. Convert each line to an object
    x b. Total the persons bills
    x c. Write the persons name along with the total to a new file
x 3. Keep track of the running total
x 4. Display total users processed and total bills calculated
'''
# ways to evade column headers from popping the code
# change the seek?
#