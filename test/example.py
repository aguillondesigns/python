from random import randint

class Player:
    id: int = 0
    name: str = None
    score: int = 0

    def __init__(this, name, id):
        this.name = name
        this.id = id
        this.score = 0

class Round:
    id: int = 0
    scores: dict = {}

    def __init__(this):
        this.id = 0
        this.scores = {}

class Game:
    # Game configuration
    number_players = 3
    rounds = 5

    # Stored game data
    players: list[Player] = []
    round_data: list[Round] = []
    winner: Player = None

    def __init__(this):
        this.players = []
        this.round_data = []
        this.winner = None

    def run(this):
        # Get the players
        this.__get_players()

        # Run the rounds
        this.__run_rounds()

        # determine the winner
        for round in this.round_data:
            print(f"Round: {round.id}")
            high_score = 0
            winner = None
            for player_number in round.scores:
                print(player_number, round.scores[player_number])
                current_score = round.scores[player_number]
                if current_score > high_score:
                    high_score = current_score
                    winner = player_number
            for player in this.players:
                if player.id == winner:
                    print(f"{player.name} wins the round!")


    def __get_players(this):
        while len(this.players) < this.number_players:
            name = ""
            while name == "":
                name = input("Enter player name: ")
            this.players.append(Player(name, len(this.players) + 1))

    def __run_rounds(this):
        id = 1
        while id <= this.rounds:
            round = Round()
            round.id = id
            for player in this.players:
                random_number = randint(5,25)
                player.score = random_number
                round.scores[player.id] = random_number
            this.round_data.append(round)
            id += 1
            

        # Create a random number for each player

        # Save that in the round data



game = Game()
game.run()