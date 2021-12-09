import arcade
from game import constants
from game.gameView import GameView
from game.instructionsView import InstructionsView

class MenuView(arcade.View):
    """class manages the menu view"""

    def __init__(self):
        super().__init__()
        """ This is run once when we switch to this view """
        self.texture = arcade.load_texture(constants.OPEN_GAME_SPRITE)
        self.click_sound = arcade.load_sound(constants.CLICK_SOUND)
    
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text(constants.SCREEN_TITLE, self.window.width / 2-2, self.window.height / 2+210,
                        arcade.color.BLACK, font_size=25, anchor_x="center",font_name= constants.DEFAULT_FONT, bold= True)
        arcade.draw_text("Click I for Instructions", self.window.width / 2+113, self.window.height / 2-25,
                        arcade.color.BLACK, font_size=12, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("Click Spacebar to play", self.window.width / 2+113, self.window.height / 2-75,
                        arcade.color.BLACK, font_size=12, anchor_x="center",font_name= constants.DEFAULT_FONT)
        arcade.draw_text("Click Esc to exit game", self.window.width / 2+113, self.window.height / 2-50,
                        arcade.color.BLACK, font_size=12, anchor_x="center",font_name= constants.DEFAULT_FONT)

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        if key == arcade.key.SPACE:
            arcade.play_sound(self.click_sound)
            game_view = GameView()
            game_view.setup()
            self.window.show_view(game_view)
        elif key == arcade.key.I:
            arcade.play_sound(self.click_sound)
            game_view = InstructionsView()
            self.window.show_view(game_view)
        elif key == arcade.key.ESCAPE:
            arcade.play_sound(self.click_sound)
            arcade.exit()
