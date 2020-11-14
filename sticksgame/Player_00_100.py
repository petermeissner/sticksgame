import random
from sticksgame import Player, Molds

class Player_00_100(Player):
    def players_strategy(self, molds: Molds) -> bool:
        choice = random.choices(population=(True, False), weights=(0, 1))[0]
        return choice
