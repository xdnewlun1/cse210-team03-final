import arcade
import random
from game import constants 
from game.apple import Apple
from game.barbell import Barbell
from game.carrot import Carrot
from game.donut import Donut
from game.gameOverView import GameOver
from game.player import Player
from game.pizza import Pizza
from game.backMusic import BackgroundMusic
#from game.explosion import Explosion
from game.gameTime import Game_timer

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
        self.barbell_list = None
        self.carrot_list = None
        self.donut_list = None
        self.pizza_list = None
        self.wall_list = None
        self.background = None
        self.backgroundMusic = None
        self.chewing = None
        #explosion
        #self.explosions_list = None

        self.timer = 0.0
        self.timer_output = "00:00:00"

        # separate variable that holds the player sprite
        self.player_sprite = None
        self.score = 150

        # preload animation frames
        # self.explosion_texture_list = []
        # # LOAD TEH EXPLOSIONS FROM A SPRITE SHEET
        # columns = 16
        # count = 60
        # sprite_width= 256
        # sprite_height = 256
        # file_name = constants.EXPLOSION_FILE_NAME
        # self.explosion_texture_list = arcade.load_spritesheet(file_name, sprite_width, sprite_height,columns,count )


    def setup(self):
        """set up the game here. call this function to restart the game """
        # sprite list create the object instance for individual 
        self.player_list = arcade.SpriteList()
        self.apple_list = arcade.SpriteList()
        self.barbell_list = arcade.SpriteList()
        self.carrot_list = arcade.SpriteList()
        self.donut_list = arcade.SpriteList()
        self.pizza_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash= True)
        self.background = arcade.load_texture(constants.BACKGROUND_SPRITE)
        self.backgroundMusic = BackgroundMusic()
        self.chewing = arcade.load_sound(constants.CHEWING)
        self.explosions_list = arcade.SpriteList()

        self.timer = 0.0
        self.timer_output = "00:00:00"

        # keep track of score
        self.score = 150 #set to zero here and in initialize 
        
        # set up player sprite
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)
        self.create_food()
        self.create_barbell()

        #don't show the mouse pointer # snowflake ex
        self.window.set_mouse_visible(False)

        # create the physics engine by setting it to arcades physcis engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        """render the screen and draw the sprites"""
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0,0,constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.background)
        self.apple_list.draw()
        self.barbell_list.draw()
        self.player_list.draw()
        self.donut_list.draw()
        self.pizza_list.draw()
        self.carrot_list.draw()
        self.explosions_list.draw()
        
        # put text on screen 
        output = f"Weight: {self.score}"
        arcade.draw_text(output, 650, 560, arcade.color.WHITE, 16)

        # set up timer output the time text
        arcade.draw_text(self.timer_output, 10, 560, arcade.color.WHITE, 16)

        # mute text on screen
        mute_text = "Push M to Mute"
        arcade.draw_text(mute_text,20,20,arcade.csscolor.WHITE), 16

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        self.player_sprite.on_key_press(key,modifiers)
        self.backgroundMusic.on_key_press(key, modifiers)

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
        self.barbell_list.update()
        self.explosions_list.update()

        self.apple_collision()
        self.carrot_collision()
        self.donut_collision()
        self.pizza_collision()
        self.barbell_collision()

        #self.game_timer(delta_time)
        self.timer += delta_time
        self.timer_output = Game_timer.update_timer(self.timer)

        #self.check_timer(self.timer_output)
        Game_timer.check_timer(self.timer_output)

        # physics engine
        self.physics_engine.update()

    def check_health(self, score):
        """Checks the weight of the player to determines gameOver"""
        if self.score >= 600:
            view = GameOver(self.minutes, self.seconds)
            self.window.show_view(view)
    
    def create_food(self):
        for a in range(random.randrange(5,25)):
            # Image create by Zach 
            apple = Apple()
            self.apple_list.append(apple)
            """Creates the carrot """
        for c in range(random.randrange(5,25)):
            carrot = Carrot()
            self.carrot_list.append(carrot)
    
        """Creates the donut """
        for d in range(random.randrange(5,25)):
            donut = Donut()
            self.donut_list.append(donut)

        """Creates the pizza"""
        for p in range(random.randrange(5,25)):
            pizza = Pizza()
            self.pizza_list.append(pizza)

    def create_barbell(self):
        """Creates the barbell"""
        for a in range(random.randrange(5,25)):
            barbell = Barbell()
            self.barbell_list.append(barbell)

    def apple_collision(self):
        """determines collision of player sprite and food """
        apple_hit = arcade.check_for_collision_with_list(self.player_sprite, self.apple_list)
        for apple in apple_hit:
            arcade.play_sound(self.chewing, constants.SFX_VOLUME)
            apple.reset_pos()
            self.score += 5
            self.check_health(self.score)

    def barbell_collision(self):
        """determines collision of player sprite and food """
        barbell_hit = arcade.check_for_collision_with_list(self.player_sprite, self.barbell_list)
        for barbell in barbell_hit:
            barbell.reset_pos()
            self.score -= 5
            self.check_health(self.score)

    def carrot_collision(self):
        """determines collision of player sprite and food """
        carrot_hit = arcade.check_for_collision_with_list(self.player_sprite, self.carrot_list)
        for carrot in carrot_hit:
            arcade.play_sound(self.chewing, constants.SFX_VOLUME)
            carrot.reset_pos()
            self.score += 5
            self.check_health(self.score)

    def donut_collision(self):   
        """determines collision of player sprite and food """
        donut_hit = arcade.check_for_collision_with_list(self.player_sprite, self.donut_list)
        for donut in donut_hit:
            arcade.play_sound(self.chewing, constants.SFX_VOLUME)
            donut.reset_pos()
            self.score += 15
            self.check_health(self.score)

    def pizza_collision(self):
        """determines collision of player sprite and food """
        pizza_hit = arcade.check_for_collision_with_list(self.player_sprite, self.pizza_list)
        for pizza in pizza_hit:
            arcade.play_sound(self.chewing, constants.SFX_VOLUME)
            pizza.reset_pos()
            self.score += 10
            self.check_health(self.score)
            

