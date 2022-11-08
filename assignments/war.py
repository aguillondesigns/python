import os
clear = lambda: os.system('cls')

from curses.ascii import isdigit
from random import randint, random

# Keep track of who won the round
roundWinners = {}
playerWins = {}
currentRound = 1

# Ask how many players
numberPlayers = 0

def askPlayerCount():
    print("How many players?")
    players = input()
    if players.isdigit():
        return int(players)
    else:
        askPlayerCount()

# Ask player names
playerNames = []

def getPlayerName():
    print("Enter player name:")
    name = input()
    if (len(name) <= 0):
        print("Invalid Name")
        getPlayerName()
    else:
        playerNames.append(name)

# Gets all player names
def getPlayers():
    while len(playerNames) < numberPlayers:
        getPlayerName()
    print(playerNames)

# Draws our initial screen
def showGreeting():
    clear()
    print("Welcome to Terminal War!")
    print("This is a simple text based battle between several players.")
    print("As your host, I will pick random numbers for each Player and we shall see who wins!")

def getRandomNumber():
    return randint(1,21)

def runRound():
    clear()
    roundData = {}
    global roundWinners, currentRound, playerWins
    print("Round " + str(currentRound))
    if (currentRound > 1):
        for player in playerNames:
            if player in playerWins:
                print(player + "'s wins: " + str(playerWins[player]))
        print()
    currentRound += 1
    for player in playerNames:
        playerScore = getRandomNumber()
        roundData[player] = playerScore
        print(player + " has a score of " + str(playerScore))
    # Before we can determine the high score, need to see if there is a tie
    highScore = max(roundData.values())
    highScoreUser = max(roundData, key=roundData.get)
    print(highScoreUser + " wins the round with a score of " + str(highScore) + "!")
    roundWinners[currentRound] = highScoreUser
    if highScoreUser in playerWins:
        playerWins[highScoreUser] += 1
    else:
        playerWins[highScoreUser] = 1
    print("Play another round? y/n")
    anotherRound = input()
    if anotherRound == "y":
        return True
    else:
        return False

def showWinSummary():
    global playerWins
    maxScore = max(playerWins.values())
    maxUser = max(playerWins, key=playerWins.get)
    clear()
    print("The winner of the match goes to: " + maxUser + 
        " who won " + str(maxScore) + " rounds!")

def RunGame():
    showGreeting()
    global numberPlayers
    numberPlayers = askPlayerCount()
    getPlayers()
    runAgain = runRound()
    while runAgain:
        runAgain = runRound()
    showWinSummary()

RunGame()

