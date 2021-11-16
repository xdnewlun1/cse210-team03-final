import arcade
from game.director import Director

def main():
    window = Director()
    window.Setup()
    arcade.run()
main()