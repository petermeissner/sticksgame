# Imports

import pprint
import pandas as pd

from sticksgame import Game, Player


# Options 
pd.set_option('display.max_columns', None)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    game = Game(Player, Player, Player)
    game.play()
    pprint.pprint(game.stats())
    pprint.pprint(game.log.log)

