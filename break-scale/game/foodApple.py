import arcade
from game import constants
import random
class Apple(arcade.Sprite): # this needs to have parameter of arcade library and sprite 
    """This class represents the food on our screen. it is a chld class
    of the arcade librarys Sprite class"""

    #def __init__(self, arcade, sprite):
        # self.arcade = arcade
        # self.sprite = sprite
        # self.x = 0
        # self.y = 0
    #def reset_pos to reset the position calling self
    """reset the food to a random spot above the screen"""

    def reset_pos(self):
        # self.y = constants.SCREEN_HEIGHT + 50
        # self.x = random.randrange(constants.SCREEN_WIDTH)
        self.center_y = random.randrange(constants.SCREEN_HEIGHT + 30, constants.SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(constants.SCREEN_WIDTH)


        
    def update(self, delta_time):
            # define update to move the food 
        """move the food and see if the food has fallen off the 
        bottom of the screen. if so reset it"""
        
        # self.y -= constants.FOOD_FALL_SPEED * delta_time
        # if(self.y < 0):
        #     self.reset_pos()
        self.center_y -= 1

        
        # did the food go off the screen If so, pop back to the top.
        # or remove it
        if self.top < 0:
            self.reset_pos()

    """
        Copy Falling Snow to be falling apples that collide with the player and give points.
        Colision
        https://upload.wikimedia.org/wikipedia/commons/3/3e/Applepix.png
    """