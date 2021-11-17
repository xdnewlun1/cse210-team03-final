import arcade
from game import constants 
#from game.player import Player
#from game.foodApple import Apple 

class Director(arcade.Window):
    def __init__(self):
        """Set up the game . Call this function to restart the game """
        # call the parent class and set up the window 
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH, constants.SCREEN_TITLE)
        
        # our scene object to initialize and draw all at once 

        # notes about scene object the sprite list would be different
        # we would set scene.add_sprite_list("Player")

        # create the variable that will hold the sprite list 
        # These are list that keep track of sprites
        # Each sprite should go into a list set to none 
        # player_sprite_list, apple_sprite_list, donut_sprite_list, spaital hashing off
        # wall_list_sprite turn on spatial hashing
        self.player_sprite_list = None
        self.apple_sprite_list = None

        # separate variable that holds the player sprite
        self.player_sprite = None

        # set background color or set the tileMap
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """set up the game here. call this function to restart the game """
        # initialize in init_ add in set up for different levels

        # setup the cameras

        # sprite list create the object instance 
        self.player_sprite_list = arcade.SpriteList()
        self.apple_sprite_list = arcade.SpriteList()

        # set up the player instance, 
        # character scaling to .50 for 50 % of the screen
        # set up player specifically placing it at the coordinates center x 
        # and center y coordinates 
        
        # keep track of score
        #self.score = 0 set to zero here and in initialize 

        # create the ground 
        # this shows using a loop to place multiple sprites horizontally 

        # create the trees on the ground
        # this shows using a coordinate list to place sprites. 
        # create  the physics engine 
        # collisions food 

        # --- set up the wall instance
        # create horizontal rows of boxes
            # top edges
            # bottom edges
        # create vertical columns of boxes
            # left
            # right
            # create a box in the middle 

        # create the food instance
            # position the food
            # add the food to the list
        
        # create the unhealthy food instance
            # position the food
            # add the food to the list 

        # set up the background
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # create the physics engine by setting it to arcades physcis engine
        # and adding the player sprite and the scene sprite list to walls

        
    
    def on_draw(self):
        """render the screen"""
        # clear the screen to the background color
        arcade.start_render()

        # draw our sprites or call draw the scene draw ()
        #self.player_list.draw()
        #self.apple_list.draw()

        # activate the game camera

        # draw our score on the screen, scrolling it with the viewport

    def on_update(self, delta_time):
        """movement and game logic"""
        # move the player with the physics engine
        # see if we hit any food
        #loop through each food we hit if any and remove it 
        #position the camera
        pass 

    # where do we put the key presses ??? in player?  input? or leave here? 
    def on_key_press(self, key, key_modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        pass
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
