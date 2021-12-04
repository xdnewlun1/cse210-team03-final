from game import constants
import arcade
import csv
from operator import itemgetter

class GameOver(arcade.View):
    """ View to show when game is over """

    def __init__(self, minutes, sec):
        """ This is run once when we switch to this view """
        super().__init__()
        self.minutes = minutes
        self.new_name = "___"
        self.sec = sec
        print("Opened GameEndScreen")
        #self.texture = arcade.load_texture(constants.PLAYER_SPRITE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)
        self.score_list = []
        with open(constants.SCOREBOARD_FILE, newline='') as f:
            reader = csv.reader(f)
            self.score_list = list(reader)
        for item in self.score_list[1:]:
            item[1] = int(item[1])
            item[2] = int(item[2])
        self.check_scoreboard()
        
    def on_draw(self):
        """ Draw this view """
        arcade.start_render()
        arcade.set_background_color(arcade.color.PURPLE)
        #self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
        #                        constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("Scoreboard", 10, constants.SCREEN_HEIGHT - 100, arcade.color.BLACK, 79, width=400, align="center", font_name="Kenney Blocks")
        i = 0
        for item in self.score_list:
            if '_' in item[0]:
                arcade.draw_text(self.new_name, 10, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), arcade.color.BLACK, 25, width=200, align="left", font_name="Kenney Blocks")
            else:
                arcade.draw_text(item[0].capitalize(), 10, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), arcade.color.BLACK, 25, width=200, align="left", font_name="Kenney Blocks")
            i += 1
        i = 0
        for item in self.score_list:
            time = (f"{item[1]}:{item[2]}")
            if(self.score_list.index(item) == 0):
                arcade.draw_text(time, 242, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), arcade.color.BLACK, 25, width=200, align="left", font_name="Kenney Blocks")
            else:
                arcade.draw_text(time, 300, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), arcade.color.BLACK, 25, width=200, align="left", font_name="Kenney Blocks")
            i += 1
        
        self.not_ready = False
        for item in self.score_list:
            if '_' in item[0]:
                self.not_ready = True
                if '_' in self.new_name:
                    arcade.draw_text("ENTER YOUR INITIALS! BKSP to Delete a letter!", 10, 10, arcade.color.BLACK, 15, width=600, align="center", font_name="Kenney Blocks")
                else:
                    arcade.draw_text("Press ENTER to Confirm! BKSP to Delete!", 10, 10, arcade.color.BLACK, 15, width=600, align="center", font_name="Kenney Blocks")
        if self.not_ready == False:
            arcade.draw_text("Press ESC to Leave!", 10, 10, arcade.color.BLACK, 20, width=600, align="center", font_name="Kenney Blocks") 

    #def on_mouse_press(self, _x, _y, _button, _modifiers):
        # """ If the user presses the mouse button, re-start the game. """
        # game_view = GameView()
        # game_view.setup()
        # self.window.show_view(game_view)
    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """
        #self.player_sprite.update(key)
        if key >= 97 and key <= 122:
            self.new_name = self.new_name.replace("_", chr(key), 1)
        if key == arcade.key.ESCAPE:
            arcade.exit()
        if key == arcade.key.BACKSPACE:
            self.new_name = "___"
        if key == arcade.key.ENTER and self.new_name[2] != "_":
            for item in self.score_list:
                if item[0] == "___":
                    item[0] = self.new_name
            self.update_scoreboard()

    def on_update(self, delta_time):
        pass

    def check_scoreboard(self):
        new_time = ["___", self.minutes, self.sec]
        self.score_list.append(new_time)
        self.score_list = sorted(self.score_list[1:], key=itemgetter(1,2,0), reverse=True)
        print(self.score_list)
        self.score_list.insert(0, ["name", "min", "sec"])
        if len(self.score_list) > 11:
            self.score_list.remove(self.score_list[11])
    
    def update_scoreboard(self):
        with open(constants.SCOREBOARD_FILE, "w") as score_file:
            for item in self.score_list:
                print(f"{item[0]},{item[1]},{item[2]}", file=score_file)
        
