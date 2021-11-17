import arcade
from game import constants 
import random # for snowflake example
import math # for snowflake example
from game.fallingSnow import Snowflake # for snowflake example 
#from game.player import Player
#from game.foodApple import Apple 

# Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.

class Director(arcade.Window):
    def __init__(self):
        """Set up the game . Call this function to restart the game """
        # call the parent class and set up the window 
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_WIDTH, constants.SCREEN_TITLE)
        
        # our scene object to initialize and draw all at once 
        self.scene = None
        # notes about scene object the sprite list would be different
        # we would set scene.add_sprite_list("Player") add it to setup
        
        # create the variable that will hold the sprite list 
        # These are list that keep track of sprites
        # Each sprite should go into a list set to none 
        # player_sprite_list, apple_sprite_list, donut_sprite_list, spaital hashing off
        # wall_list_sprite turn on spatial hashing
        # self.player_list = None
        # self.apple_sprite_list = None
        # self.snowflake_sprite_list = None # snowflake example

        # separate variable that holds the player sprite
        self.player_sprite = None

        # our physics engine

        # set background color or set the tileMap
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """set up the game here. call this function to restart the game """
        # initialize in init_ add in set up for different levels
        # initialize the set up for scene objects
        # we would set scene.add_sprite_list("Player")
        self.scene = arcade.Scene()
        # setup the cameras

        # create the sprite list for scene object scene
        self.scene.add_sprite_list("Player")
        self.scene.add_sprite_list("Apple")
        self.scene.add_sprite_list("Walls")
        self.scene.add_sprite_list("Snowflake")

        # sprite list create the object instance for individual 
        # self.player_list = arcade.SpriteList()
        # self.apple_sprite_list = arcade.SpriteList()

        # set up the player instance, 
        # character scaling to .50 for 50 % of the screen
        # set up player specifically placing it at the coordinates center x 
        # and center y coordinates 
        image_source = "break-scale/game/resources/images/player/alienGreen_stand.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y =150
        self.scene.add_sprite("Player", self.player_sprite)
    
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
            # create it need width and height
            # position the food need center x and center y
            # add the food to the list
        
        # create the unhealthy food instance
            # position the food
            # add the food to the list 

        # snowflake example 

        # explosion 
        self.snowflake_list = []# snowflake ex

        for i in range(20):
            # create snowflake instance
            snowflake = Snowflake()

            # randomly position snowflake
            snowflake.x = random.randrange(constants.SCREEN_WIDTH)
            snowflake.y = random.randrange(constants.SCREEN_HEIGHT + 200)

            snowflake.size = random.randrange(10)
            snowflake.speed = random.randrange(30,40)
            snowflake.angle = random.uniform(math.pi, math.pi * 2)

            # add snowflake to snowflake list 
            self.snowflake_list.append(snowflake)
            

        #don't show the mouse pointer # snowflake ex
        self.set_mouse_visible(False)

        # set up the background
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # create the physics engine by setting it to arcades physcis engine
        # and adding the player sprite and the scene sprite list to walls

    def on_draw(self):
        """render the screen"""
        # clear the screen to the background color
        arcade.start_render()

        # draw our sprites or call draw the scene draw ()
        self.scene.draw()
        #self.apple_list.draw()

        # put text on screen 
            # score 
            # draw text box

        # put instructions on screen 
        # instructions = "Move left or right arrows to get eat food"
        # arcade.draw_text(instructions, 10,90, arcade.color.WHITE,12)
        
       
        # activate the game camera

        # draw our score on the screen, scrolling it with the viewport
        # player explodes
        # snowflake example
        # draw the current position of each snowflake
        for snowflake in self.snowflake_list:
            arcade.draw_circle_filled(snowflake.x, snowflake.y, snowflake.size, arcade.color.WHITE)

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = - constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ called whenever the user lets off a previously pressed key basically stops the player from moving"""
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """called whenever the mouse moves"""   
        pass
    def on_mouse_press(self, x,y,delta_x, delta_y):
        """called whenthe user pressesthe mouse button"""
        pass
    def on_mouse_release(self, x,y,delta_x, delta_y):
        """called when a u ser releases a mouse button"""
        pass

    def on_update(self, delta_time):
        """movement and game logic"""
        #position the camera
        # snowflake example 
        # Animate all the snowflake falling
        for snowflake in self.snowflake_list:
            snowflake.y -= snowflake.speed * delta_time

            # check if snowflake has fallen below screen
            if snowflake.y < 0 :
                snowflake.reset_pos()
            
            # some math to make the snowflake move side to side
            snowflake.x += snowflake.speed * math.cos(snowflake.angle) * delta_time
            snowflake.angle += 1 * delta_time
            
        # move the player with the physics engine


        # move player without physics list 
        # move player
        # remove these lines in physics enige is moving player
        self.player_sprite.center_x += self.player_sprite.change_x
        self.player_sprite.center_y += self.player_sprite.change_y

        #check for out of bounds
        if self.player_sprite.left < 0:
            self.player_sprite.left = 0
        elif self.player_sprite.right > constants.SCREEN_WIDTH -1:
            self.player_sprite.right = constants.SCREEN_WIDTH -1

        if self.player_sprite.bottom < 0:
            self.player_sprite.bottom = 0
        elif self.player_sprite.top > constants.SCREEN_HEIGHT -1 :
            self.player_sprite.top = 0
        
        # Call update on all sprites (The sprites don't do much in this
        # example though.) # see if we hit any food 

        # Generate a list of all sprites that collided with the player.

        #loop through each food  see if we hit  change it, and add to score if any and remove it 
        

        