# Imports

import random
import pprint
import re

import pandas as pd
pd.set_option('display.max_columns', None)

from sticksgame import Molds, Log, now, Player




class Game:
    """
    The game class storing logs, players and mold state as well as providing game loop execution over players
    """
    players = None
    players_class = None
    molds = None
    log = None

    def __init__(self, *args):
        """
        Create a Game

        :param number_of_players: int, number of players
        """

        # set up log
        self.log = Log(game_id = now()[0:19].replace("-", "").replace(":", ""))

        # set up molds object
        self.molds = Molds()

        # set up players
        self.players = []
        self.players_class = []
        for i, pl in enumerate(args):
            p = pl(player_i=i, log=self.log)
            self.players_class.append(p.__class__.__name__)
            self.players.append(p)

    def play(self):
        """
        start game loop execution
        :return:
        """
        player_result = ""
        i = 0
        while player_result != "won":
            player_result = self.players[i % len(self.players)].players_turn(self.molds)
            i = i + 1

    def stats(self)->dict:
        d = dict()
        d['mean_stick_distance'] = sum([p.sticks for p in self.players]) / (len(self.players) - 1)
        d['dice_throws'] = len(self.log.log)
        d['player_turns'] = len(list(filter(lambda x: x['dice_n'] == 1, self.log.log)))
        d['player_points'] = [p.sticks for p in self.players]
        d['player_class'] = self.players_class
        return d




# main
if __name__ == '__main__':
    game = Game(Player, Player, Player)
    game.play()
    pprint.pprint(game.stats())

