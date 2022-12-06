import lib.Bills as bills
import subprocess
import locale
import os

clear = lambda: os.system('cls')
locale.setlocale(locale.LC_ALL, '')

class FileProcessor:
    Filename = ''
    OutputFile = ''
    subtotals = {}

    def __init__(this, filename, outfile):
        this.Filename = filename
        this.OutputFile = outfile
        this.InitTotals()   # Setup our placeholders dictionary

    def InitTotals(this):
        this.subtotals['runningTotal'] = 0
        this.subtotals['recordsProcessed'] = 0
        this.subtotals['phoneTotal'] = 0
        this.subtotals['electricTotal'] = 0
        this.subtotals['houseTotal'] = 0
        this.subtotals['waterTotal'] = 0
        this.subtotals['foodTotal'] = 0

    def Sanitize(this, item):
        return str(item).strip()

    def ProcessFile(this):
        # Prepare the output file
        this.PrepareOutputFile()
        # Read our data set
        this.ReadFileData()
        # Render the output
        this.RenderOutput()

    def ReadFileData(this):
        # Grab the number of lines
        f = open(this.Filename, 'r')
        numberLines = len(f.readlines())
        f.seek(0, 0)    # Reset our file position
        line = 0
        while line < numberLines:
            currentLine = this.Sanitize(f.readline())
            pieces = this.GetSanitizedPieces(currentLine)
            if str(pieces[1]).isdigit():    # ensure the second column consists of numbers
                userBills = bills.Bills(
                    pieces[0],  # name
                    int(pieces[1]),  # phone
                    int(pieces[2]),  # house
                    int(pieces[3]),  # electric
                    int(pieces[4]),  # water
                    int(pieces[5]))  # food
                #print(userBills.name, "'s total: ", userBills.total())  # User line out, move out of here?
                this.StoreUserBills(userBills)
                this.SaveRowToFile(userBills.name, userBills.total())
            line += 1

    def StoreUserBills(this, userBills):
        this.subtotals['runningTotal'] += userBills.total()
        this.subtotals['recordsProcessed'] += 1
        this.subtotals['phoneTotal'] += int(userBills.phone)
        this.subtotals['electricTotal'] += int(userBills.electric)
        this.subtotals['houseTotal'] += int(userBills.house)
        this.subtotals['waterTotal'] += int(userBills.water)
        this.subtotals['foodTotal'] += int(userBills.food)

    def GetSanitizedPieces(this, line):
        pieces = str(line).split(',')
        cleaned = []
        for piece in pieces:
            cleaned.append(this.Sanitize(piece))
        return cleaned

    def SaveRowToFile(this, name, total):
        f = open(this.OutputFile, 'a')
        f.write(name + ',' + str(total) + '\n')
        f.close()

    def PrepareOutputFile(this):
        # clean out the output file
        f = open(this.OutputFile, 'w')
        f.close()

    def RenderOutput(this):
        clear()
        print("Total Records Processed: ", this.subtotals['recordsProcessed'])
        print("Total of all users: ", locale.currency(this.subtotals['runningTotal'], grouping=True))
        print()
        print("Bill Breakdown: ")
        print("Housing:  ", locale.currency(this.subtotals['houseTotal'], grouping=True))
        print("Phone:    ", locale.currency(this.subtotals['phoneTotal'], grouping=True))
        print("Electric: ", locale.currency(this.subtotals['electricTotal'], grouping=True))
        print("Food:     ", locale.currency(this.subtotals['foodTotal'], grouping=True))
        print("Water:    ", locale.currency(this.subtotals['waterTotal'], grouping=True))

# Call the csv generator
subprocess.call('csvGenerator.py', shell=True)

# Clear the screen to prepare for our data ouput
clear() 
processor = FileProcessor('test.csv', 'totals.txt')
processor.ProcessFile()