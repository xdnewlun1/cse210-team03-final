import arcade
from game import constants 
from game.apple import Apple
#from game.barbell import Barbell
from game.carrot import Carrot
from game.donut import Donut
from game.gameOverView import GameOver
from game.player import Player
from game.pizza import Pizza



class GameView(arcade.View):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    """
    def __init__(self):
        """The class constructor.
        
        Args:
        player_list The player sprite 
        self.apple_list SpriteList - list of food set to None
        #self.barbell_list SpriteList - list of food set to None
        self.carrot_list SpriteList - list of food set to None
        self.donut_list SpriteList - list of food set to None
        self.pizza_list SpriteList - list of food set to None
        self.wall_list SpriteList - list of food set to None
        self.timer to track the time spent on the game set to zero
        self.timer_output = "00:00:00"
        self.player_sprite The player sprite 
        self.score = 150 starting weight
        """
        super().__init__()

        # Each sprite should go into a list set to none 
        self.player_list = None
        self.apple_list = None
        #self.barbell_list = None
        self.carrot_list = None
        self.donut_list = None
        self.pizza_list = None
        self.wall_list = None
        
        self.timer = 0.0
        self.timer_output = "00:00:00"

        # separate variable that holds the player sprite
        self.player_sprite = None
        self.score = 150

        # set background color or set the tileMap
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """set up the game here. call this function to restart the game """
        # sprite list create the object instance for individual 
        self.player_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()
        #self.barbell_list = arcade.SpriteList()
        self.carrot_list = arcade.SpriteList()
        self.donut_list = arcade.SpriteList()
        self.pizza_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash= True)
        
        self.timer = 0.0

        # keep track of score
        self.score = 150 #set to zero here and in initialize 
        
        # set up player sprite
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)

        self.create_apple()
        self.create_carrot()
        self.create_donut()
        self.create_pizza()
        #self.create_barbell()

        # explosion 
        
        #don't show the mouse pointer # snowflake ex
        self.window.set_mouse_visible(False)

        # set up the background
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # create the physics engine by setting it to arcades physcis engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """render the screen and draw the sprites"""
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

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        self.player_sprite.on_key_press(key,modifiers)

    def on_key_release(self, key, modifiers):
        """ called whenever the user lets off a previously pressed key basically stops the player from moving"""
        self.player_sprite.on_key_release(key,modifiers)

    def on_update(self, delta_time):
        """movement and game logic"""
        # Generate a list of all sprites that collided with the player.
        self.player_list.update()
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

        # physics engine
        self.physics_engine.update()

    def check_health(self,score):
        """Checks the weight of the player to determines gameOver"""
        if self.score >= 600:
            view = GameOver(self.minutes, self.seconds)
            self.window.show_view(view)
            
    def create_apple(self):
        """Creates the apple"""
        for a in range(20):
            # Image create by Zach 
            apple = Apple()
            self.apple_list.append(apple)

    # def create_barbell(self):
    """Creates the barbell"""
    #     for a in range(5):
    #         barbell = Barbell()
    #         self.barbell_list.append(barbell)

    def create_carrot(self):
        """Creates the carrot """
        for c in range(20):
            carrot = Carrot()
            self.carrot_list.append(carrot)
    
    def create_donut(self):
        """Creates the donut """
        for d in range(20):
            donut = Donut()
            self.donut_list.append(donut)

    def create_pizza(self): 
        """Creates the pizza"""
        for p in range(20):
            pizza = Pizza()
            self.pizza_list.append(pizza)

    def apple_collision(self):
        """determines collision of player sprite and food """
        apple_hit = arcade.check_for_collision_with_list(self.player_sprite, self.apple_list)
        for apple in apple_hit:
            apple.remove_from_sprite_lists()
            self.score += 5
            self.check_health(self.score)

    # def barbell_collision(self):
    """determines collision of player sprite and food """
    #     barbell_hit = arcade.check_for_collision_with_list(self.player_sprite, self.barbell_list)
    #     for barbell in barbell_hit:
    #         barbell.reset_pos()
    #         self.score -= 5
    #         self.check_health(self.score)

    def carrot_collision(self):
        """determines collision of player sprite and food """
        carrot_hit = arcade.check_for_collision_with_list(self.player_sprite, self.carrot_list)
        for carrot in carrot_hit:
            carrot.reset_pos()
            self.score += 1
            self.check_health(self.score)

    def donut_collision(self):   
        """determines collision of player sprite and food """
        donut_hit = arcade.check_for_collision_with_list(self.player_sprite, self.donut_list)
        for donut in donut_hit:
            donut.reset_pos()
            self.score += 15
            self.check_health(self.score)

    def pizza_collision(self):
        """determines collision of player sprite and food """
        pizza_hit = arcade.check_for_collision_with_list(self.player_sprite, self.pizza_list)
        for pizza in pizza_hit:
            pizza.reset_pos()
            self.score += 10
            self.check_health(self.score)
            
    
