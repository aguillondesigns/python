import random

class ColumnConfig:
    columnType = ''
    numCharacters = 0
    minValue = 0    # min value for integer type
    maxValue = 0    # max value for integer type

    def __init__(this, columnType, numCharacters = 0, minValue = 0, maxValue = 0):
        if this.isValidColumnType(columnType) == False:
            exit("Invalid column type defined, use (string or in)")

        this.columnType = columnType

        # For integers, set the min and max values
        if columnType == 'int':
            this.minValue = minValue
            this.maxValue = maxValue

        # For strings, set the number of characters
        if columnType == 'string':
            this.numCharacters = numCharacters

    def isValidColumnType(this, columnType):
        validTypes = ['string', 'int']
        return columnType in validTypes

    def GetValue(this):
        if this.columnType == 'string':
            return this.GetRandomString()
        if this.columnType == 'int':
            return this.GetRandomInt()

    def GetRandomString(this):
        newString = ''
        while len(newString) < this.numCharacters:
            newString += this.GetRandomCharacter()
        return newString

    def GetRandomCharacter(this):
        characters = 'abcdefghijklmnopqrstuvwxyz' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        return random.choice(characters)

    def GetRandomInt(this):
        return random.randint(this.minValue, this.maxValue)