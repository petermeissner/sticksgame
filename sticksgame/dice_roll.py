import random

def dice_roll() -> int:
    """
    random number, either: 1, 2, 3, 4, 5, or 6 each with p = 1/6
    """
    return random.choices((1, 2, 3, 4, 5, 6))[0]
