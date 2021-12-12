import arcade
from game import constants

class Explosion(arcade.Sprite):
    """this class creates an explosion"""
    def __init__(self, texture_list):
        super().__init__()

        # start at the first frame
        self.textures = texture_list
        self.current_texture = 0
    
    def update(self):
        # update to the next frame of explosion
        # then delete the sprite
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()
            # end game 
            constants.GAME_OVER = True
        

