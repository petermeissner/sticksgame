# Imports

import pprint
import pandas as pd

from sticksgame import Game, Player, write_to_db



# Options 
pd.set_option('display.max_columns', None)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

  for i in range(100):
    game = Game(Player, Player, Player)
    game.play()
    
    write_to_db(
      df         = game.log.to_df(), 
      db_name    = 'games.db', 
      table_name = 'games_data'
    )
    stats = game.stats()
    
    write_to_db(
      pd.DataFrame(
        {
          'game_id':             [stats['game_id']], 
          'dice_throws':         [stats['dice_throws']], 
          'mean_stick_distance': [stats['mean_stick_distance']],
          'player_turns':        [stats['player_turns']]
        }
        ), 
        db_name    = 'games.db', 
        table_name = 'games'
      )

    write_to_db(
      pd.DataFrame(
        {
          'game_id':             stats['game_id'], 
          'dice_throws':         stats['player_class'], 
          'mean_stick_distance': stats['player_id'],
          'player_points':       stats['player_points']
        }
        ), 
        db_name    = 'games.db', 
        table_name = 'game_players'
      )

    print(f"\r\t{i}", end="")
    
  print("")


