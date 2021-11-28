from game import constants
#from game.director import GameView
import arcade
import csv

class GameOver(arcade.View):
    """ View to show when game is over """

    def __init__(self, minutes, sec):
        """ This is run once when we switch to this view """
        super().__init__()
        self.minutes = minutes
        self.sec = sec
        #self.texture = arcade.load_texture(constants.PLAYER_SPRITE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)
        self.score_list = []
        with open(constants.SCOREBOARD_FILE, newline='') as f:
            reader = csv.reader(f)
            self.score_list = list(reader)
        print(self.score_list)
        self.check_scoreboard()
        


    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        #self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        #                        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("Scoreboard", 10, constants.SCREEN_HEIGHT - 100, arcade.color.BLACK, 79, width=400, align="center", font_name="Kenney Blocks")
        for item in self.score_list:
            arcade.draw_text(item[0].capitalize(), 10, constants.SCREEN_HEIGHT - (100 + (40 * (self.score_list.index(item) + 1))), arcade.color.BLACK, 25, width=200, align="left", font_name="Kenney Blocks")
        for item in self.score_list:
            time = (f"{item[1]}:{item[2]}")
            if(self.score_list.index(item) == 0):
                arcade.draw_text(time, 242, constants.SCREEN_HEIGHT - (100 + (40 * (self.score_list.index(item) + 1))), arcade.color.BLACK, 25, width=200, align="left", font_name="Kenney Blocks")
            else:
                arcade.draw_text(time, 300, constants.SCREEN_HEIGHT - (100 + (40 * (self.score_list.index(item) + 1))), arcade.color.BLACK, 25, width=200, align="left", font_name="Kenney Blocks")

    #def on_mouse_press(self, _x, _y, _button, _modifiers):
        # """ If the user presses the mouse button, re-start the game. """
        # game_view = GameView()
        # game_view.setup()
        # self.window.show_view(game_view)

    def check_scoreboard(self):
        for listee in self.score_list[1:]:
            if int(listee[1]) <= self.minutes:
                if int(listee[2]) <= self.sec:
                    self.score_list.insert(self.score_list.index(listee),["", self.min, self.sec])
        if len(self.score_list) > 11:
            self.score_list.remove(self.score_list[11])
