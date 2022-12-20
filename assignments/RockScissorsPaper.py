import random
import os
clear = lambda: os.system('cls')
MAX_PLAYERS = 2

class Player:
    # Players name
    name = ''
    # Players score
    score = 0
    # Players round choices
    choices = {}

    def __init__(this, name):
        this.name = name
        this.choices = {}
        this.score = 0

    # num - number of rounds we need choices for
    def set_random_choices(this, num):
        i = 1
        while i <= num:
            this.choices[i] = random.choice(['rock','scissors','paper'])
            i += 1

    def get_round_choice(this, round):
        return this.choices[round]

class RockScissorsPaper:
    player_a = (Player)
    player_b = (Player)
    rounds = 0

    def __get_round_winner(this, round):
        player_a_choice = this.player_a.get_round_choice(round)
        player_b_choice = this.player_b.get_round_choice(round)
        if player_a_choice == player_b_choice:
            return 'draw'

        if player_a_choice == 'rock':
            if player_b_choice == 'scissors':
                return this.player_a
            if player_b_choice == 'paper':
                return this.player_b

        if player_a_choice == 'scissors':
            if player_b_choice == 'rock':
                return this.player_b
            if player_b_choice == 'paper':
                return this.player_a

        if player_a_choice == 'paper':
            if player_b_choice == 'rock':
                return this.player_a
            if player_b_choice == 'scissors':
                return this.player_b

    def __get_players(this):
        players = []
        # Continue grabbing players until we have 2 valid player
        while len(players) < MAX_PLAYERS:
            id = len(players) + 1
            playerName = this.get_player(id)
            # Good player name, save it
            if len(playerName) > 0:
                players.append(playerName)
        # Setup our players now
        this.player_a = Player(players[0])
        this.player_b = Player(players[1])

    def __get_player(this, id):
        clear()
        # String interpolation
        print(f"What is the name of Player {id} ?")
        name = input()
        return name

    def __get_rounds(this):
        clear()
        while this.rounds <= 0:
            print("How many rounds would you like to play? (3, 5, 7)")
            choice = input()
            valid_options = ['3', '5', '7']
            if choice in valid_options:
                this.rounds = int(choice)

    def __setup_random_choices(this):
        this.player_a.set_random_choices(this.rounds)
        this.player_b.set_random_choices(this.rounds)

    def __output_round_data(this, round, winner):
        if winner == 'draw':
            print(f"Round {round} is a draw.")
        else:
            print(f"{winner.name} wins the round! " + 
            f"({this.player_a.name}: {this.player_a.get_round_choice(round)} vs {this.player_b.name}: {this.player_b.get_round_choice(round)})")

    def __process_rounds(this):
        clear()
        currentRound = 1
        while currentRound <= this.rounds:
            winner = this.__get_round_winner(currentRound)
            if winner == 'draw':
                this.player_a.score += 1
                this.player_b.score += 1
            if winner == this.player_a:
                this.player_a.score += 2
            if winner == this.player_b:
                this.player_b.score += 2

            # Output round data
            this.output_round_data(currentRound, winner)
            currentRound += 1
        print("")
        print("Final Score:")
        print(f"{this.player_a.name} has a score of {this.player_a.score}")
        print(f"{this.player_b.name} has a score of {this.player_b.score}")

        this.__save_match_data()

    def __save_match_data(this):
        filename = "rsp_scores.csv"
        f = open(filename, 'a')
        f.write(f"{this.player_a.name},{this.player_a.score},{this.player_b.name},{this.player_b.score}\n")
        f.close

    def run(this):
        this.__get_players()
        this.__get_rounds()
        this.__setup_random_choices()
        this.__process_rounds()

game = RockScissorsPaper()
game.run()



'''
Get Player Names
Ask how many rounds to play
Setup players with random choices for each round
'''
