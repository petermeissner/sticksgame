import random
from sticksgame import Player, Molds

class Player_50_50(Player):
    def players_strategy(self, molds: Molds) -> bool:
        choice = random.choices(population=(True, False), weights=(0.5, 0.5))[0]
        return choice


