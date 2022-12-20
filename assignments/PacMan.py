class PacMan:
    number_players = 0

    def __init__(this, number_players):
        this.number_players = number_players
        this.initialize()

    def __initialize(this):
        this.velocity = 7
        this.enemies = 3
        this.enemy_velocity = 8

    def run(this):
        print("running")

game = PacMan(2)
game.run()


