import arcade
from game import constants
from game.gameView import GameView

class InstructionsView(arcade.View):
    """This is to show different views for a windows
    """
    
    def __init__(self):
        super().__init__()
        """ This is run once when we switch to this view """
        self.texture = arcade.load_texture(constants.INSTRUCTIONS_SPRITE)
        # Add Sound
        self.click_sound = arcade.load_sound(constants.CLICK_SOUND)

    def on_show(self):
        """ This is run once when we switch to this view """
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("Instructions", self.window.width / 2+130, self.window.height / 2+200,
                        arcade.color.WHITE, font_size=constants.DEFAULT_FONT_SIZE*2.2, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("How to play", self.window.width / 2+85, self.window.height / 2+95,
                        arcade.color.BLACK, font_size=20, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("It's raining food! Every item you touch you", self.window.width / 2+85, self.window.height / 2+45,
                        arcade.color.RED, font_size=12, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("you can't help but eat. Once you reach 600 pounds", self.window.width / 2+85, self.window.height / 2+20,
                        arcade.color.RED, font_size=12, anchor_x="center",font_name= constants.DEFAULT_FONT)                 
        arcade.draw_text("you'll explode! So aim for the barbells and avoid", self.window.width / 2+85, self.window.height / 2-5,
                        arcade.color.RED, font_size=12, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("the unhealthy foods especially. Good Luck!", self.window.width / 2+85, self.window.height / 2-30,
                        arcade.color.RED, font_size=12, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("Controls", self.window.width / 2+85, self.window.height / 2-70,
                        arcade.color.BLACK, font_size=20, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("Move Left", self.window.width / 2+85, self.window.height / 2-150,
                        arcade.color.BLACK, font_size=17, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("Move Right", self.window.width / 2+85, self.window.height / 2-240,
                        arcade.color.BLACK, font_size=17, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("Press Spacebar to play", self.window.width / 2+85, self.window.height / 2-290,
                        arcade.color.RED, font_size=14, anchor_x="center",font_name= constants.DEFAULT_FONT)

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """

        if key == arcade.key.SPACE:
            arcade.play_sound(self.click_sound)
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
    
        elif key == arcade.key.ESCAPE:
            arcade.play_sound(self.click_sound)
            arcade.exit()
