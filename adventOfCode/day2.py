'''
A,X = Rock = 1
B,Y = Paper = 2
C,Z = Scissors = 3

Lost = 0
Draw = 3
Win = 6
'''

def getStringValue(letter):
    if letter == 'A' or letter == 'X':
        return 'rock'
    if letter == 'B' or letter == 'Y':
        return 'scissors'
    if letter == 'C' or letter == 'Z':
        return 'paper'

def getRoundScore(oponent, player):
    oValue = getStringValue(oponent)
    pValue = getStringValue(player)
    winner = getWinner(oValue, pValue)

def getWinner(o, p):
    if o == 'A' and p == 'Z':
        return o
    

with open("day2.data", 'r') as f:
    lines = len(f.readlines())
    f.seek(0,0)
    line = 0

    while line < lines:
        data = f.readline().strip()
        # If we are dealing with a number
        choices = data.split(' ')

        roundScore = getRoundScore(choices[0].strip(), choices[1].strip())        

        line += 1