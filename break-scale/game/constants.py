import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Break the Scale"

#constants used to scale our sprites from their original size 
CHARACTER_SCALING = 3
TILE_SCALING = 0.5
FOOD_SCALING = 0.5
PATH = os.path.dirname(os.path.abspath(__file__))

# do we need gravity? 
GRAVITY = 1
# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5

# FOOD COUNT 
FOOD_COUNT = 250
APPLE_COUNT = 15
FOOD_FALL_SPEED = 0.25

# PLAYER STARTING POSITION

# LAYER NAMES FROM TILEMAP

# file path
#PATH = os.path.dirname(os.path.abspath(__file__))
