import arcade
from game import constants

class Player(arcade.Sprite):
    """ Player Class """
    """This class represents the player on our screen. it is a child class
    of the arcade library Sprite class"""

    # Set up parent class
    def __init__(self) : 
        image_source = "break-scale/game/resources/images/player/test_player1.png"
        super().__init__(image_source, constants.CHARACTER_SCALING)
        self.center_x = 400
        self.center_y = 100

    def update(self):
        """ Move the player """
        # Move player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > constants.SCREEN_WIDTH -1:
            self.right = constants.SCREEN_WIDTH -1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > constants.SCREEN_HEIGHT -1 :
            self.top = 0
        # move player without physics list 
        # move player
        # remove these lines in physics engine is moving player
        

        #check for out of bounds
