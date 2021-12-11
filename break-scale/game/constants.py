import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Break the Scale"

#constants used to scale our sprites from their original size 
CHARACTER_SCALING = 2.5
TILE_SCALING = 0.5
FOOD_SCALING = 0.5

#Sprites
PATH = os.path.dirname(os.path.abspath(__file__))
PLAYER_SPRITE = PATH + "/resources/images/player/player_sprite.png"
PLAYER_LEFT_SPRITE = PATH + "/resources/images/player/player_sprite_left.png"
APPLE_SPRITE = PATH + "/resources/images/food/apple_sprite.png"
BARBELL_SPRITE = PATH + "/resources/images/food/Dumbbell_sprite.png"
CARROT_SPRITE = PATH + "/resources/images/food/carrot_sprite.png"
DONUT_SPRITE = PATH + "/resources/images/food/donut_sprite.png"
PIZZA_SPRITE = PATH + "/resources/images/food/pizza_sprite.png"
OPEN_GAME_SPRITE = PATH + "/resources/images/background/Open_Game_Sprite1.png"
INSTRUCTIONS_SPRITE = PATH + "/resources/images/background/Instructions_Sprite.png"
BACKGROUND_SPRITE = PATH + "/resources/images/background/basic_background.png"
SCOREBOARD_BACKGROUND =PATH + "/resources/images/background/scoreboard.png"

# explosion info
EXPLOSION_FILE_NAME = PATH + "/resources/images/explosion.png"
EXPLOSION_TEXTURE_COUNT = 60
COLUMNS: 16
COUNT = 60
SPRITE_WIDTH = 256
SPRITE_HEIGHT = 256

#SCOREBOARD FILE
SCOREBOARD_FILE = PATH + "/resources/scoreboard.csv"

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 4

# FOOD
GRAVITY = 1
GRAVITY_SPEED = 2

DEFAULT_FONT = "Kenney Blocks"
DEFAULT_FONT_SIZE = 20

# PLAYER 
LEFT_FACING = 0
RIGHT_FACING = 1
NOT_MOVING = 2

#Sounds
CLICK_SOUND = PATH + "/resources/sounds/click.mp3"
BACKGROUND_MUSIC = PATH + "/resources/sounds/background_music.mp3"
CHEWING = PATH + "/resources/sounds/chewing.mp3"
RICK = PATH + "/resources/sounds/rick-roll.mp3"

#VOLUME
MUSIC_VOLUME = 0.1
SFX_VOLUME = 0.15
MUTED_VOLUME = 0

