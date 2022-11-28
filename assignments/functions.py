import os
clear = lambda: os.system('cls')

# Switch to script directory
def setCurrentDirectory():
    absPath = os.path.abspath(__file__)
    directoryName = os.path.dirname(absPath)
    os.chdir(directoryName)

# Bool - lets us know if a file is available for reading
def fileExists(filename):
    try:
        f = open(filename, "r")
        f.close()
        return True
    except:
        return False

# This function assumes the file exists
def printFileContents(filename):
    clear()
    print("Contents of:", filename)
    f = open(filename, 'r')
    print(f.read())
