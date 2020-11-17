import random
from sticksgame import Player, Molds

class Player_33_66(Player):
    def players_strategy(self, molds: Molds) -> bool:
        choice = random.choices(population=(True, False), weights=(1/3, 2/3))[0]
        return choice

