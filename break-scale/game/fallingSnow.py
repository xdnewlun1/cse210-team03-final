from game import constants
import random

class Snowflake:
    """ EAch instance of this class represents a single snowflake
        based on a drawing filleed circles"""

    def __init__(self) :
        self.x = 0
        self.y = 0
    def reset_pos(self):
        # reset flake to random position above screen
        self.y = random.randrange(constants.SCREEN_HEIGHT, constants.SCREEN_HEIGHT + 100)
        self.x = random.randrange(constants.SCREEN_WIDTH)