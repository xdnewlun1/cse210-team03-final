import arcade
from game.director import Director

def main():
    window = Director()
    window.setup()
    arcade.run()

    
main()