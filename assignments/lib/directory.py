import os

def setCurrentDirectory():
    absPath = os.path.abspath(__file__)
    directoryName = os.path.dirname(absPath)
    os.chdir(directoryName)