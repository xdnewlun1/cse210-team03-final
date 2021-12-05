from game import constants
import arcade
import csv
from operator import itemgetter

class GameOver(arcade.View):
    """ View to show when game is over """

    def __init__(self, minutes, sec):
        """ This is run once when we switch to this view """
        """ The variables for the Players time from the game is set, the New_Name is set and all colors for the page are set """
        super().__init__()
        self.minutes = minutes
        self.new_name = "___"
        self.sec = sec
        self.text_color = arcade.color.BLACK
        self.back_color = arcade.color.DARK_ORCHID
        self.click_sound = arcade.load_sound(constants.CLICK_SOUND)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        # Initalize the score_list which is imperative to the rest of the page
        # Open the SCOREBOARD_FILE. Read file contents into self.score_list
        # Convert all numbers in the new self.score_list to ints
        # Run check_scoreboard()
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
        """ 
            First we draw the SCOREBOARD text for the top of the screen
            Next we run through three loops, the first loop we draw all of the Initials from the list, if the initals in the list are equal to ___ then it displays the user input
            that it will start looking for until the use presses enter and confirms.
            The next set of loops draws all the times from the self.score_list with no login needed because the times dont change
            The use of the i = 0 statement and counting for the placement on the screen makes it so duplicate names, or times arent places on top of eachother from use of the self.score_list.index() command I used at the beginning
            The final loop checks to see what the text at the bottom needs to say. If it has a name that needs to be entered it will tell you to enter it, if no name is needed or ENTER has been pressed
            then it will switch to tell you to leave the game using ESC. not_ready is the tracking for if the ENTER key is pressed.
        """
        arcade.start_render()
        arcade.set_background_color(self.back_color)
        arcade.draw_text("Scoreboard", 10, constants.SCREEN_HEIGHT - 100, self.text_color, 79, width=400, align="center", font_name="Kenney Blocks")
        i = 0
        for item in self.score_list:
            if '_' in item[0]:
                arcade.draw_text(self.new_name, 10, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), self.text_color, 25, width=200, align="left", font_name="Kenney Blocks")
            else:
                arcade.draw_text(item[0].capitalize(), 10, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), self.text_color, 25, width=200, align="left", font_name="Kenney Blocks")
            i += 1
        i = 0
        for item in self.score_list:
            time = (f"{item[1]}:{item[2]}")
            if(self.score_list.index(item) == 0):
                arcade.draw_text(time, 242, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), self.text_color, 25, width=200, align="left", font_name="Kenney Blocks")
            else:
                arcade.draw_text(time, 300, constants.SCREEN_HEIGHT - (100 + (40 * (i + 1))), self.text_color, 25, width=200, align="left", font_name="Kenney Blocks")
            i += 1
        
        self.not_ready = False
        for item in self.score_list:
            if '_' in item[0]:
                self.not_ready = True
                if '_' in self.new_name:
                    arcade.draw_text("ENTER YOUR INITIALS! BKSP to Delete a letter!", 10, 10, self.text_color, 15, width=600, align="center", font_name="Kenney Blocks")
                else:
                    arcade.draw_text("Press ENTER to Confirm! BKSP to Delete!", 10, 10, self.text_color, 15, width=600, align="center", font_name="Kenney Blocks")
        if self.not_ready == False:
            arcade.draw_text("Press ESC to Leave!", 10, 10, self.text_color, 20, width=600, align="center", font_name="Kenney Blocks") 

    def on_key_press(self, key, modifiers):
        """ called whenever a key on the keyboard is pressed
        for a list of keys, see:https://api.arcade.academy/en/latest/arcade.key.html """

        """ 
            Check for key presses of the letters to input them into the new_name variable which will change the view on the screen to have these new characters included
            If you presse Backspace the entire self.new_name variable is returned to the ___ state so the user can re enter the initials as needed
            If you press enter and the final character of self.new_name doesnt equal "_" then it will officially set the name in the score_list and update the scoreboard file.
        """
        if key >= 97 and key <= 122:
            for item in self.score_list:
                if '_' in item[0]:
                    arcade.play_sound(self.click_sound)
                    self.new_name = self.new_name.replace("_", chr(key), 1)
        if key == arcade.key.ESCAPE:
            arcade.play_sound(self.click_sound)
            arcade.exit()
        if key == arcade.key.BACKSPACE:
            arcade.play_sound(self.click_sound)
            self.new_name = "___"
        if key == arcade.key.ENTER and self.new_name[2] != "_":
            arcade.play_sound(self.click_sound)
            for item in self.score_list:
                if item[0] == "___":
                    item[0] = self.new_name
            self.update_scoreboard()

    def on_update(self, delta_time):
        pass

    def check_scoreboard(self):
        #Function addes the current players new time to the score_list ignoring wether or not it is in the top 10 times
        #self.score_list is sorted first by Minutes, then Seconds, then Name and reversed. This is done by using the index of the sub lists for soring in the key attribute
        #The list is check to see if there is an 11th item in the list, if so then it is removed. This is how we weed out a new player score if it doesnt deserve to be in, or remove the previous score at #10
        new_time = ["___", self.minutes, self.sec]
        self.score_list.append(new_time)
        self.score_list = sorted(self.score_list[1:], key=itemgetter(1,2,0), reverse=True)
        self.score_list.insert(0, ["name", "min", "sec"])
        if len(self.score_list) > 11:
            self.score_list.remove(self.score_list[11])
    
    def update_scoreboard(self):
        """
            Update scoreboard opens the scoreboard.csv file and deletes all the contents, it then writes the new self.score_list into the file so that it can be read correctly
            once the scoreboard class is needed once again.
        """
        with open(constants.SCOREBOARD_FILE, "w") as score_file:
            for item in self.score_list:
                print(f"{item[0]},{item[1]},{item[2]}", file=score_file)
        
