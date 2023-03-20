from random import randint

class Player:
    player_name: str = None
    player_score: int = 0

    def __init__(this, name: str, score: int):
        this.player_name = name
        this.player_score = score

class Game:
    players: list[Player] = []

    def __init__(this):
        this.players = []

    def run(this):
        this.__get_players(2)

    def __get_players(this, qty: int = 2):
        while len(this.players) < qty:
            name = this.__get_player()
            this.players.append(Player(name, randint(1,10)))

    def __get_player(this):
        name = ""
        while len(name) < 2:
            name = input("Player Name: ")
            if len(name) > 2:
                return name
            else:
                input("Invalid name, press enter to try again...")
      

game = Game()
game.run()
highest_score = 0
winner = None
for player in game.players:
    print(player.player_name, player.player_score)
    if player.player_score > highest_score:
        highest_score = player.player_score
        winner = player.player_name

print(winner, highest_score)