import arcade
#from game.player import Player
#from game.foodApple import Apple 
from game import constants

class Director(arcade.Window):
    def __init__(self):
        """Set up the game . Call this function to restart the game """
        # call the parent class and set up the window 
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH, constants.SCREEN_TITLE)
        # our scene object

        # create the sprite list 
        # These are list that keep track of sprites
        # Each sprite should go into a list set to none 
        self.player_list = None
        self.apple_sprite_list = None
        # separate variable that holdsthe player sprite
        self.player_sprite = None
        # set background color
        arcade.set_background_color(arcade.css.color.CORNFLOWER_BLUE)

    def setup(self):
        """set up the game here. call this function to restart the game """
        # setup the cameras

        # sprite list 

        # --- set up the wall s
        # crete horizontal rows of boxes
            # top edges
        # create vertical columns of boxes
            # left
            # right
            # create a box in the middle 
        # set up the player , specifically playing it at the coordinates
        self.player_list = arcade.SpriteList()
        # keep track of score
        #self.score = 0 set to zero here and in initialzie 

        # create the food instance
            # position the food
            # add the food to the list 
        # create the unhealthy food instance
            # position the food
            # add the food to the list 
        # set up the background
        arcade.set_background_color(arcade.css.color.CORNFLOWER_BLUE)
        # create the ground 
        # this shows using a loop to place multiple sprites horizotally 
        #put some trees on the ground
        # this shows using a coordinate list to place sprites. 
        # create  the physics engine 
        # collisions food 
    
    def on_draw(self):
        """render the screen"""
        # clear the screen to the background color
        arcade.start_render()
        # activate the game camera
        # draw the scene
        # draw our score on the screen, scrolling it with the viewport
    def on_update(self, delta_time):
        """movement and game logic"""
        # move the player with the physics engine
        # see if we hit any food
        #loop through each food we hit if any and remove it 
        #position the camera
        pass 
    def on_key_press(self, key, key_modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
    def on_key_release(self, key, key_modifiers):
        """ called whenever the user lets off a previously pressed key"""
        pass
    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """called whenever the mouse moves"""   
        pass
    def on_mouse_press(self, x,y,delta_x, delta_y):
        """called whenthe user pressesthe mouse button"""
        pass
    def on_mouse_release(self, x,y,delta_x, delta_y):
        """called when a u ser releases a mouse button"""
        pass