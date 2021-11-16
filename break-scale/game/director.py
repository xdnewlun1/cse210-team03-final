import arcade
from game.player import player
from game import constants
class Director:
    def __init__(self):

        """Set up the game here. Call this function to restart the game."""

        # Call the parent class and set up the window
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # Create the Sprite lists
        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.

        # Separate variable that holds the player sprite

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Setup the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

    # Sprite lists

    # -- Set up the walls
        # Create horizontal rows of boxes
        # Top edge
        # Create vertical columns of boxes
            # Left
            # right
            # Create boxes in the middle
 
    # Set up the player, specifically placing it at these coordinates.
    # Keep track of the score
        self.score = 0

        # Create the food instance
            # Position the food
            # Add the food to the lists
        # Create the unhealthy food instance
            # Position the food
            # Add the food to the lists
    
    # set up the background
    arcade.set_background_color(arcade.color.AMAZON)

    # Create the ground
    # This shows using a loop to place multiple sprites horizontally

    
    # Put some trees on the ground
        # This shows using a coordinate list to place sprites

    # Create the 'physics engine' 

    # collisions food 

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here