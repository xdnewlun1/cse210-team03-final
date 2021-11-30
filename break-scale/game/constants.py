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
APPLE_SPRITE = PATH + "/resources/images/food/Apple_sprite.png"
CARROT_SPRITE = PATH + "/resources/images/food/Carrot_sprite.png"
DONUT_SPRITE = PATH + "/resources/images/food/Donut_sprite.png"
PIZZA_SPRITE = PATH + "/resources/images/food/Pizza_sprite.png"
OPEN_GAME_SPRITE = PATH + "/resources/images/background/Open_Game_Sprite.png"
INSTRUCTIONS_SPRITE = PATH + "/resources/images/background/Instructions_Sprite.png"


# do we need gravity? 
GRAVITY = 1
# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5

# FOOD COUNT 
#FOOD_COUNT = 250
#APPLE_COUNT = 50
FOOD_FALL_SPEED = 0.25

DEFAULT_FONT = "Kenney Blocks"
DEFAULT_FONT_SIZE = 20
# PLAYER STARTING POSITION

# LAYER NAMES FROM TILEMAP

# file path
#PATH = os.path.dirname(os.path.abspath(__file__))
