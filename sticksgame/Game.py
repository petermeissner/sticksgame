# Imports

from typing import List
from itertools import cycle

import pprint

import pandas as pd
pd.set_option('display.max_columns', None)


from sticksgame import Molds, Log, now, Player




class Game:
    """
    The game class storing logs, players and mold state as well as providing game loop execution over players
    """
    players: List       = None
    players_class: List = None
    molds: Molds        = None
    log: Log            = None
    game_id: str        = None


    def __init__(self, *args):
        """
        Create a Game

        :param number_of_players: int, number of players
        """

        # set up game id
        self.game_id = now()[0:19].replace("-", "").replace(":", "")

        # set up log
        self.log     = Log(game_id = self.game_id)

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
        Start game loop execution
        :return: None
        """
        player_result = ""
        player_cycle = cycle(self.players)
        
        # loop over players - check for win condition
        while player_result != "won":
            
            # get next player
            current_player = next(player_cycle)
            player_result  = "start"
            
            # let player play and choose her actions            
            while player_result == "start" or player_result == "again":
                player_result  = current_player.players_turn(self.molds)
                


    def stats(self)->dict:
        
        # declare dict for storage
        d = dict()
        
        # fill storage
        d['player_id']           = list(range(len(self.players)))
        d['game_id']             = self.game_id
        d['mean_stick_distance'] = sum([p.sticks for p in self.players]) / (len(self.players) - 1)
        d['dice_throws']         = len(self.log.log)
        d['player_turns']        = len(list(filter(lambda x: x['dice_n'] == 1, self.log.log)))
        d['player_points']       = [p.sticks for p in self.players]
        d['player_class']        = self.players_class

        # return
        return d




# main
if __name__ == '__main__':
    game = Game(Player, Player, Player)
    game.play()
    pprint.pprint(game.stats())

