import sys
import arcade
from game.actor import Actors  # need to add player to actors
class inputService:

    def on_key_press(self,key,modifiers,constants):
        if key == arcade.key.LEFT or key == arcade.key.A:
            actor.player_sprite.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            actor.player_sprite.change_x = constants.PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.LEFT or key == arcade.key.A:
            actor.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            actor.player_sprite.change_x = 0