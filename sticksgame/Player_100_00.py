import random
from sticksgame import Player, Molds

class Player_100_00(Player):
    def players_strategy(self, molds: Molds) -> bool:
        choice = random.choices(population=(True, False), weights=(1, 0))[0]
        return choice
