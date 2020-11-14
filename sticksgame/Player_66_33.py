import random
from sticksgame import Player, Molds

class Player_66_33(Player):
    def players_strategy(self, molds: Molds) -> bool:
        choice = random.choices(population=(True, False), weights=(2/3, 1/3))[0]
        return choice
