import arcade
from game import constants
import random


class Apple(arcade.Sprite): 
    """This class represents the food on our screen. it is a child class
    of the arcade library Sprite class"""

    def update(self):
            # define update to move the food 
        """move the food and see if the food has fallen off the 
        bottom of the screen. if so reset it"""
        
        self.center_y -= 1

        
        # did the food go off the screen If so, pop back to the top.
        # or remove it
        if self.top < 0:
            # self.reset_pos()
            self.bottom = constants.SCREEN_HEIGHT

    """
        Copy Falling Snow to be falling apples that collide with the player and give points.
        Colision
        https://upload.wikimedia.org/wikipedia/commons/3/3e/Applepix.png"""