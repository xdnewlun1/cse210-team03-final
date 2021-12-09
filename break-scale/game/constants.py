import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Break the Scale"

#constants used to scale our sprites from their original size 
CHARACTER_SCALING = 3
TILE_SCALING = 0.5
FOOD_SCALING = 0.5

#Sprites
PATH = os.path.dirname(os.path.abspath(__file__))
PLAYER_SPRITE = PATH + "/resources/images/player/test_player1.png"
APPLE_SPRITE = PATH + "/resources/images/food/apple_sprite.png"
BARBELL_SPRITE = PATH + "/resources/images/food/Dumbbell_sprite.png"
CARROT_SPRITE = PATH + "/resources/images/food/carrot_sprite.png"
DONUT_SPRITE = PATH + "/resources/images/food/donut_sprite.png"
PIZZA_SPRITE = PATH + "/resources/images/food/pizza_sprite.png"
OPEN_GAME_SPRITE = PATH + "/resources/images/background/Open_Game_Sprite1.png"
INSTRUCTIONS_SPRITE = PATH + "/resources/images/background/Instructions_Sprite.png"
BACKGROUND_SPRITE = PATH + "/resources/images/background/AdobeStock_284556987.png"
SCOREBOARD_BACKGROUND =PATH + "/resources/images/background/purple.png"

#SCOREBOARD FILE
SCOREBOARD_FILE = PATH + "/resources/scoreboard.csv"

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 10

# FOOD
GRAVITY = 1
GRAVITY_SPEED = 1

DEFAULT_FONT = "Kenney Blocks"
DEFAULT_FONT_SIZE = 20
# PLAYER STARTING POSITION

#Sounds
CLICK_SOUND = PATH + "/resources/sounds/click.mp3"
BACKGROUND_MUSIC = PATH + "/resources/sounds/background_music.mp3"
CHEWING = PATH + "/resources/sounds/chewing.mp3"
RICK = PATH + "/resources/sounds/rick-roll.mp3"

#VOLUME
MUSIC_VOLUME = 0.1
SFX_VOLUME = 0.05
MUTED_VOLUME = 0

