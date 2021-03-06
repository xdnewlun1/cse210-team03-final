import arcade
from game import constants

class Player(arcade.Sprite):
    """ Player Class """
    """This class represents the player on our screen. it is a child class
    of the arcade library Sprite class"""

    def __init__(self) : 
        """The class constructor."""
        super().__init__(constants.PLAYER_SPRITE, constants.CHARACTER_SCALING)
        # location of player
        self.center_x = 400
        self.center_y = 50

        self.scale = constants.CHARACTER_SCALING
        self.textures = []

        texture = arcade.load_texture(constants.PLAYER_LEFT_SPRITE)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_LEFT_SPRITE,
                                        flipped_horizontally=True)
        self.textures.append(texture)
        texture = arcade.load_texture(constants.PLAYER_SPRITE)
        self.textures.append(texture)

        # BY DEFAULT FACE RIGHT                                 
        self.texture = texture

    def on_key_press(self, key, modifier):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = - constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = constants.PLAYER_MOVEMENT_SPEED 
        elif key == arcade.key.ESCAPE:
            arcade.exit()
        
            
    def on_key_release(self, key, modifier):
        """ called whenever the user lets off a previously pressed key basically stops the player from moving"""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.change_x = 0

    def update(self):
        """ Move the player """
        # Move player
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[constants.LEFT_FACING]
        elif self.change_x > 0:
            self.texture = self.textures[constants.RIGHT_FACING]
        elif self.change_x == 0:
            self.texture = self.textures[constants.NOT_MOVING]

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > constants.SCREEN_WIDTH -1:
            self.right = constants.SCREEN_WIDTH -1
        # check for out of bounds
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > constants.SCREEN_HEIGHT -1 :
            self.top = 0
