import arcade
from game import constants
import random


class Apple(arcade.Sprite): 
    """This class represents the food on our screen. it is a child class
    of the arcade library Sprite class"""

    def __init__(self) : 
        super().__init__(constants.APPLE_SPRITE, constants.FOOD_SCALING)

    def create_apple(self):
        for a in range(20):
            #create the apple instane by Zach
            apple = Apple(constants.APPLE_SPRITE, constants.FOOD_SCALING)
            # position the apple
            apple.center_x = random.randrange(constants.SCREEN_WIDTH)
            apple.center_y = random.randrange(constants.SCREEN_HEIGHT)
            #self.apple_list.append(apple)

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