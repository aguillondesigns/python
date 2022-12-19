from random import choice, randint
import os
import time
clear = lambda: os.system('cls')

class Player:
    # Players name
    Name = ''
    # Players score
    Score = 0
    # Players round choices
    Choices = {}

    def __init__(this, name):
        this.Name = name

    # num - number of rounds we need choices for
    def SetRandomChoices(this, num):
        print(this.Name)
        i = 1
        while i <= num:
            this.Choices[i] = choice(['rock','scissors','paper'])
            i += 1

    def GetRoundChoice(this, round):
        return this.Choices[round]

class RockScissorsPaper:
    PlayerA = Player
    PlayerB = Player
    Rounds = 0

    def GetWinner(this, a, b):
        if a == 'rock':
            if b == 'scissors':
                return a
            if b == 'paper':
                return b
            return 'draw'

        if a == 'scissors':
            if b == 'rock':
                return b
            if b == 'paper':
                return a
            return 'draw'

        if a == 'paper':
            if b == 'rock':
                return a
            if b == 'scissors':
                return b
            return 'draw'

    def GetPlayers(this):
        players = []
        # Continue grabbing players until we have 2 valid player
        while len(players) < 2:
            id = len(players) + 1
            playerName = this.GetPlayer(id)
            # Good player name, save it
            if len(playerName) > 0:
                players.append(playerName)
        # Setup our players now
        this.PlayerA = Player(players[0])
        this.PlayerB = Player(players[1])

    def GetPlayer(this, id):
        #clear()
        print("What is the name of Player " + str(id) + "?")
        name = input()
        return name

    def GetRounds(this):
        #clear()
        while this.Rounds <= 0:
            print("How many rounds would you like to play? (3, 5, 7)")
            choice = input()
            validOptions = ['3', '5', '7']
            if choice in validOptions:
                this.Rounds = int(choice)

    def SetupRandomChoices(this):
        print("hello")
        this.PlayerA.SetRandomChoices(this.Rounds)
        playerAChoices = this.PlayerA.Choices
        print(this.PlayerA.Name, playerAChoices)
        this.PlayerB.SetRandomChoices(this.Rounds)
        playerBChoices = this.PlayerB.Choices
        print(this.PlayerB.Name, playerBChoices)
        print(playerAChoices)
        
            

        
        
def test():
    player1 = Player('Leo')
    player2 = Player('Livier')

    player1.SetRandomChoices(3)
    print(player1.Choices)

    player2.SetRandomChoices(3)
    print(player2.Choices)

    game = RockScissorsPaper()
    winner = game.GetWinner('rock', 'paper')
    print(winner)


#test()

game = RockScissorsPaper()
game.GetPlayers()
game.GetRounds()
game.SetupRandomChoices()
print(game.PlayerA.Name, game.PlayerA.Choices)
print(game.PlayerB.Name, game.PlayerB.Choices)

# game.PlayerA.SetRandomChoices(game.Rounds)
# print(game.PlayerA.Name, game.PlayerA.Choices)
# game.PlayerB.SetRandomChoices(game.Rounds)
# print(game.PlayerB.Name, game.PlayerB.Choices)


'''
Get Player Names
Ask how many rounds to play
Setup players with random choices for each round
'''
