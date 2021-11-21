import arcade
from game import constants
# player class arcade.Sprite
class Player(arcade.Sprite):
    """ Player Class """
    """This class represents the player on our screen. it is a child class
    of the arcade librarys Sprite class"""

    # Set up parent class
    def __init__(self) : 
        pass

    # define update 
    """ Move the player and remove these lines if physics engine is moving player """
        # Move player.
        # Remove these lines if physics engine is moving player.

        # Check for out-of-bounds

        # move the player with the physics engine
    

    def update(self):
        """ Move the player """
        # Move player.
        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

        # Check for out-of-bounds
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        elif self.player_sprite.right > constants.SCREEN_WIDTH -1:
            self.player_sprite.right = constants.SCREEN_WIDTH -1

        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        elif self.player_sprite.top > constants.SCREEN_HEIGHT -1 :
            self.player_sprite.top = 0
       
        # move player without physics list 
        # move player
        # remove these lines in physics enige is moving player
        

        #check for out of bounds
