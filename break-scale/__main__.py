import arcade
from game.director import Director

def main():
    """ call dirctor , setup() and arcade run()"""
    window = Director()
    window.setup()
    arcade.run()


main()
