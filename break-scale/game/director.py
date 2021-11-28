import arcade
import os
from game import constants 
from game.foodApple import Apple
from game.player import Player
from game.gameOverView import GameOver
import random
import math
from game.donut import Donut
from game.carrot import Carrot
from game.pizza import Pizza


class GameView(arcade.View):
    def __init__(self):
        """Set up the game . Call this function to restart the game """
        # call the parent class and set up the window 
        super().__init__()

        # Each sprite should go into a list set to none 
        self.player_list = None
        self.apple_list = None
        self.wall_list = None
        self.donut_list = None
        self.pizza_list = None
        self.carrot_list = None
        self.timer = 0.0
        self.timer_output = "00:00:00"

        # separate variable that holds the player sprite
        self.player_sprite = None
        self.score = 999

        # set background color or set the tileMap
        #arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """set up the game here. call this function to restart the game """
        # setup the cameras
        
        # sprite list create the object instance for individual 
        self.player_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash= True)
        self.donut_list = arcade.SpriteList()
        self.pizza_list = arcade.SpriteList()
        self.carrot_list = arcade.SpriteList()
        self.timer = 0.0

        # keep track of score
        self.score = 999 #set to zero here and in initialize 
        
        # set up player sprite
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)

        self.create_apple()
        self.create_carrot()
        self.create_donut()
        self.create_pizza()
        

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

        # explosion 
        
        #don't show the mouse pointer # snowflake ex
        self.window.set_mouse_visible(False)

        # set up the background
        #arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # create the physics engine by setting it to arcades physcis engine
        # and adding the player sprite and the scene sprite list to walls
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        


    def on_draw(self):
        """render the screen"""
        # clear the screen to the background color
        arcade.start_render()
        self.apple_list.draw()
        self.player_list.draw()
        self.donut_list.draw()
        self.pizza_list.draw()
        self.carrot_list.draw()

        # put text on screen 
        output = f"Weight: {self.score}"
        arcade.draw_text(output, 650, 560, arcade.color.WHITE, 16)

        # set up timer output the time text
        arcade.draw_text(self.timer_output, 10, 560, arcade.color.WHITE, 16)

        # put instructions on screen 
        # instructions = "Move left or right arrows to get eat food"
        # arcade.draw_text(instructions, 10,90, arcade.color.WHITE,12)


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


    def on_update(self, delta_time):
        """movement and game logic"""
        # position the camera
        
        self.player_list.update()
        
        # Generate a list of all sprites that collided with the player.
        self.apple_list.update()
        self.donut_list.update()
        self.pizza_list.update()
        self.carrot_list.update()

        # timer 
        # set up timer
        self.timer += delta_time
        # calculate minutes
        self.minutes = int(self.timer) // 60
        # calculate seconds
        self.seconds = int(self.timer) % 60
        # calculate 100s of a second
        self.seconds_100 = int((self.timer - self.seconds) * 100)
        # figure out our output
        self.timer_output = f"Time: {self.minutes:02d}:{self.seconds:02d}:{self.seconds_100:02d}"

        self.apple_collision()
        self.carrot_collision()
        self.donut_collision()
        self.pizza_collision()

        
        self.physics_engine.update()

    def check_health(self,score):
        if self.score >= 1000:
            view = GameOver(self.minutes, self.seconds)
            self.window.show_view(view)
            

    def create_apple(self):
        for a in range(20):
            #create the apple instane
            # apple image from ???
            apple = Apple(constants.APPLE_SPRITE, constants.FOOD_SCALING)
            # position the apple
            apple.center_x = random.randrange(constants.SCREEN_WIDTH)
            apple.center_y = random.randrange(constants.SCREEN_HEIGHT)
            #apple.speed = random.randrange(30,40)
            #self.all_sprites_list.append(apple)
            self.apple_list.append(apple)
    
    def create_donut(self):
        for d in range(20):
            donut = Donut(constants.DONUT_SPRITE,constants.FOOD_SCALING)
            donut.center_x = random.randrange(constants.SCREEN_WIDTH)
            donut.center_y = random.randrange(constants.SCREEN_HEIGHT)
            self.donut_list.append(donut)

    def create_carrot(self):
        for c in range(20):
            carrot = Carrot(constants.CARROT_SPRITE,constants.FOOD_SCALING)
            carrot.center_x = random.randrange(constants.SCREEN_WIDTH)
            carrot.center_y = random.randrange(constants.SCREEN_HEIGHT)
            self.carrot_list.append(carrot)
            
    def create_pizza(self): 
        for p in range(20):
            pizza = Pizza(constants.PIZZA_SPRITE,constants.FOOD_SCALING)
            pizza.center_x = random.randrange(constants.SCREEN_WIDTH)
            pizza.center_y = random.randrange(constants.SCREEN_HEIGHT)
            self.pizza_list.append(pizza)
    def apple_collision(self):
    #loop through each food  see if we hit  change it, and add to score if any and remove it 
        apple_hit = arcade.check_for_collision_with_list(self.player_sprite, self.apple_list)
        for apple in apple_hit:
            apple.remove_from_sprite_lists()
            self.score += 1
            self.check_health(self.score)
    def donut_collision(self):   
        donut_hit = arcade.check_for_collision_with_list(self.player_sprite, self.donut_list)
        for donut in donut_hit:
            donut.reset_pos()
            self.score += 15
            self.check_health(self.score)
    def pizza_collision(self):
        pizza_hit = arcade.check_for_collision_with_list(self.player_sprite, self.pizza_list)
        for pizza in pizza_hit:
            pizza.reset_pos()
            self.score += 10
            self.check_health(self.score)
    def carrot_collision(self):
        carrot_hit = arcade.check_for_collision_with_list(self.player_sprite, self.carrot_list)
        for carrot in carrot_hit:
            carrot.reset_pos()
            self.score += 5
            self.check_health(self.score)

    
            


        