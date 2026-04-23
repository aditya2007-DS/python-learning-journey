# a code to generate a random number of dice.

import random

def roll_dice():
    return random.randint(1, 6)

print("You rolled:", roll_dice())