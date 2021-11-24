import arcade
import os
from game import constants 
from game.foodApple import Apple
from game.player import Player
import random
import math

APPLE_COUNT = 15


class Director(arcade.Window):
    def __init__(self):
        """Set up the game . Call this function to restart the game """
        # call the parent class and set up the window 
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # Each sprite should go into a list set to none 
        # player_sprite_list, apple_sprite_list, donut_sprite_list, spaital hashing off
        # wall_list_sprite turn on spatial hashing
        self.player_list = None
        self.apple_list = None
        self.wall_list = None
        # self.snowflake_sprite_list = None # snowflake example

        # separate variable that holds the player sprite
        self.player_sprite = None
        self.score = 150

        #self.physics_engine = None

        # set background color or set the tileMap
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """set up the game here. call this function to restart the game """
        # setup the cameras
        
        # sprite list create the object instance for individual 
        self.player_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash= True)

        # keep track of score
        self.score = 150 #set to zero here and in initialize 
        
        # set up player sprite
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)

        # self.apple_list = []
        # apple_sprite_location = "break-scale/game/resources/images/food/Apple.png"

        # for i in range(constants.FOOD_Count):
        #     # create snowflake instance
        #     apple = arcade.Sprite(arcade, arcade.Sprite(apple_sprite_location, constants.FOOD_SCALING))
        #     apple.reset_pos()
        #     # add snowflake to snowflake list 
        #     self.apple_list.append(apple)
        #     self.scene.add_sprite("Apple", apple.sprite)
        #     self.scene.draw()

        #create the apple
        for a in range(APPLE_COUNT):
            #create the apple instane
            # apple image from ???
            apple = arcade.Sprite("break-scale/game/resources/images/food/Apple.png", constants.FOOD_SCALING)

            # position the apple
            apple.center_x = random.randrange(constants.SCREEN_WIDTH)
            apple.center_y = random.randrange(constants.SCREEN_HEIGHT)

            #apple.speed = random.randrange(30,40)

            self.apple_list.append(apple)

        # create the ground 
        # this shows using a loop to place multiple sprites horizontally 

        # create the trees on the ground
        # this shows using a coordinate list to place sprites. 
        # create the physics engine 

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

        # explosion 
        
            

        #don't show the mouse pointer # snowflake ex
        self.set_mouse_visible(False)
 
        # set up the background
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # create the physics engine by setting it to arcades physcis engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        # and adding the player sprite and the scene sprite list to walls


    def on_draw(self):
        """render the screen"""
        # clear the screen to the background color
        arcade.start_render()
        self.apple_list.draw()
        self.player_list.draw()

        # put text on screen 
        output = f"Weight: {self.score}"
        arcade.draw_text(output, 10, 550, arcade.color.WHITE, 16)

        # put instructions on screen 
        # instructions = "Move left or right arrows to get eat food"
        # arcade.draw_text(instructions, 10,90, arcade.color.WHITE,12)

        # activate the game camera

        # draw our score on the screen, scrolling it with the viewport
        # player explodes

        # for apple in self.apple_list:
        #     self.apple_list.update()

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        #self.player_sprite.update(key)
        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = - constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.ESCAPE:
            arcade.exit()

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

        # move the player with the physics engine
        
        self.player_list.update()
        
        
        #Call update on all sprites (The sprites don't do much in this
        #example though.) # see if we hit any food 

        # Generate a list of all sprites that collided with the player.
        self.apple_list.update()

        #loop through each food  see if we hit  change it, and add to score if any and remove it 

        apple_hit = arcade.check_for_collision_with_list(self.player_sprite, self.apple_list)

        for apple in apple_hit:
            apple.remove_from_sprite_lists()
            self.score += 1
        
        self.physics_engine.update()
        

        