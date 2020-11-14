

class Molds:
    """
    Class to store and handle state of the molds
    """

    occupied = None

    def __init__(self):
        self.occupied = [False, False, False, False, False]

    def apply_dice_throw(self, mold: int) -> int:
        """
        Evaluate a dice throw of a player against the current state of the molds.

        :param mold: integer stating which mold to try to put stick in
        :return: number of sticks to take
        """

        # check input
        assert mold > 0 & mold <= 6

        # 6 is for getting rid of sticks
        if (mold == 6):
            return 0

        # occupied mold means getting all the sticks
        elif (self.occupied[mold - 1] == True):

            # sum up sticks
            sticks = sum(self.occupied)

            # take them all out
            self.occupied = [False, False, False, False, False]

            # return count of sticks
            return sticks

        elif (self.occupied[mold - 1] == False):
            # put in stick
            self.occupied[mold - 1] = True

            # return zero sticks to take
            return 0
