import arcade
from game import constants
import random


class Pizza(arcade.Sprite): 
    """This class represents the food on our screen. it is a child class
    of the arcade library Sprite class"""


    # Set up parent class
    # def __init__(self) : 
    #     """reset the food to a random spot above the screen"""
    #     image_source = "break-scale/game/resources/images/food/Apple.png"
    #     super().__init__(image_source, constants.FOOD_SCALING)
    #     self.apple_count = constants.APPLE_COUNT
    def reset_pos(self):
        self.center_y = random.randrange(constants.SCREEN_HEIGHT + 30, constants.SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(constants.SCREEN_WIDTH)


    def update(self):
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
            #self.bottom = constants.SCREEN_HEIGHT

    """
        Copy Falling Snow to be falling apples that collide with the player and give points.
        Colision
        https://upload.wikimedia.org/wikipedia/commons/3/3e/Applepix.png"""