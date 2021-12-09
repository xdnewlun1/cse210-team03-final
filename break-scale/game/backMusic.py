import arcade
from arcade.sound import Sound
from game import constants
#https://api.arcade.academy/en/latest/_modules/arcade/sound.html

class BackgroundMusic():
    def __init__(self):

        self.background_music = arcade.load_sound(constants.BACKGROUND_MUSIC,True)
        
        self.muted = False
        self.mute_counter = 0
        self.background_player = arcade.play_sound(self.background_music, constants.MUSIC_VOLUME, 0, True)

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        if key == arcade.key.M:
            self.mute_counter += 1
            if self.mute_counter == 9:
                self.rick_roll = arcade.load_sound(constants.RICK, True)
                self.rick_player = arcade.play_sound(self.rick_roll, 0.1, 0, True)
                self.muted = False
            if self.mute_counter == 10:
                self.rick_roll.stop(self.rick_player)
                self.muted = False
            if self.muted == True:
                self.background_music.set_volume(constants.MUSIC_VOLUME, self.background_player)
                constants.SFX_VOLUME = 0.05
                self.muted = False
            else:
                self.background_music.set_volume(constants.MUTED_VOLUME, self.background_player)
                constants.SFX_VOLUME = 0
                self.muted = True