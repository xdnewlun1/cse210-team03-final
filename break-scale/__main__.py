import arcade
from game import constants 
from game.instructionsView import InstructionsView

def main():
    """ call dirctor , setup() and arcade run()"""
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = InstructionsView()
    window.show_view(start_view)
    arcade.run()


main()
