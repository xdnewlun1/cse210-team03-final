import arcade

class Setup:
    def __init__(self):
    # Setup the Cameras
        self.camera = arcade.Camera(self.width, self.height)
        self.gui_camera = arcade.Camera(self.width, self.height)

    # Keep track of the score
        self.score = 0