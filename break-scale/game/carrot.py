import arcade
from game import constants
import random

class Carrot(arcade.Sprite): 
    """This class represents the food on our screen. it is a child class
    of the arcade library Sprite class"""
    def __init__(self) : 
        super().__init__(constants.CARROT_SPRITE, constants.FOOD_SCALING)
        self.center_x = random.randrange(constants.SCREEN_WIDTH)
        self.center_y = random.randrange(constants.SCREEN_HEIGHT)

    def reset_pos(self):
        """Rest the fruit once it hits the bottom of the screen"""
        self.center_y = random.randrange(constants.SCREEN_HEIGHT + 30, constants.SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(constants.SCREEN_WIDTH)

    def update(self):
        """move the food and see if the food has fallen off the 
        bottom of the screen. if so reset it"""
        self.center_y -= 1

        # did the food go off the screen If so, pop back to the top.
        if self.top < 0:
            self.reset_pos()
