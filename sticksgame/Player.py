from sticksgame import Molds, dice_roll,now
import random


class Player:

    def __init__(self, player_i: int = None, log: list = None):

        if log != None:
            # create logger function
            def logger(**kwargs):
                d = dict(kwargs)
                d['player']       = self.player_i
                d['player_class'] = self.__class__.__name__
                d['timestamp']    = now()
                log.append(d)

            self.log = logger

        else:
            # create dummy logger function
            def log(**kwargs):
                pass

            self.log = log

        self.player_i = player_i

    # player index
    player_i = None

    # number of sticks
    sticks = 25

    def players_strategy(self, molds: Molds) -> bool:
        """
        Given a specific molds state this method determines if the player chooses 
        to go on and take another throw of the dices or make the next player 
        have its turn.

        :param molds: object of class Molds
        :return: boolean
        """
        choice = random.choices(population=(True, False), weights=(0.5, 0.5))[0]
        return choice

    def players_turn(self, molds: Molds) -> str:
        """

        """
        sticks_from_molds = 0
        counter = 0
        while sticks_from_molds == 0:

            # make a first non-optional, later on optional throw of the dice
            counter = counter + 1
            dice_roll_res     = dice_roll()
            mold_occupation   = molds.occupied
            mold_1 = mold_occupation[0]
            mold_2 = mold_occupation[1]
            mold_3 = mold_occupation[2]
            mold_4 = mold_occupation[3]
            mold_5 = mold_occupation[4]
            mold_6 = False
            sticks_before = self.sticks
            sticks_from_molds = molds.apply_dice_throw(dice_roll_res)

            # evaluate result of dice throw and mold occupation
            if sticks_from_molds != 0:
                # take sticks from molds and give turn to next player
                self.sticks = self.sticks + sticks_from_molds
                self.log(dice_n=counter, dice_val = dice_roll_res, 
                         mold_1=mold_1, mold_2=mold_2, mold_3=mold_3, 
                         mold_4=mold_4, mold_5=mold_5, mold_6=mold_6, 
                         sticks_before=sticks_before, sticks_after=self.sticks,
                         result = "out")
                return "out"

            else:
                # new number of sticks
                self.sticks = self.sticks - 1

                # winner?
                if (self.sticks == 0):
                    self.log(dice_n=counter, dice_val = dice_roll_res, 
                         mold_1=mold_1, mold_2=mold_2, mold_3=mold_3, 
                         mold_4=mold_4, mold_5=mold_5, mold_6=mold_6, 
                         sticks_before=sticks_before, sticks_after=self.sticks,
                             result="won")
                    return "won"

                # go on or give turn to next player?
                if self.players_strategy(molds):
                    self.log(dice_n=counter, dice_val = dice_roll_res, 
                         mold_1=mold_1, mold_2=mold_2, mold_3=mold_3, 
                         mold_4=mold_4, mold_5=mold_5, mold_6=mold_6, 
                         sticks_before=sticks_before, sticks_after=self.sticks,
                             result="next player")
                    return "next player"
                else:
                    self.log(dice_n=counter, dice_val = dice_roll_res, 
                         mold_1=mold_1, mold_2=mold_2, mold_3=mold_3, 
                         mold_4=mold_4, mold_5=mold_5, mold_6=mold_6, 
                         sticks_before=sticks_before, sticks_after=self.sticks,
                             result="again")
