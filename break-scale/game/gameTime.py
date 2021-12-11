from arcade.sound import Sound
from game import constants

class Game_timer():
    
    def update_timer(self,timer):#, delta_time):
    #     # timer 
        #timer += delta_time
    #     # calculate minutes
        self.minutes = int(timer) // 60
    #     # calculate seconds
        self.seconds = int(timer) % 60
    #     # calculate 100s of a second
        self.seconds_100 = int((timer - self.seconds) * 100)

        return f"Time: {self.minutes:02d}:{self.seconds:02d}:{self.seconds_100:02d}"
    
    def check_timer(timer):
        if timer >= "Time: 00:10:00":
            constants.GRAVITY_SPEED = 2.25
        if timer >= "Time: 00:20:00":
            constants.GRAVITY_SPEED = 2.5
        if timer >= "Time: 00:30:00":
            constants.GRAVITY_SPEED = 2.75
        if timer >= "Time: 00:40:00":
            constants.GRAVITY_SPEED = 3
        if timer >= "Time: 00:50:00":
            constants.GRAVITY_SPEED = 3.25
        if timer >= "Time: 01:00:00":
            constants.GRAVITY_SPEED = 3.5
        if timer >= "Time: 01:10:00":
            constants.GRAVITY_SPEED = 3.75
        if timer >= "Time: 01:20:00":
            constants.GRAVITY_SPEED = 4
        if timer >= "Time: 01:30:00":
            constants.GRAVITY_SPEED = 4.25
        if timer >= "Time: 01:40:00":
            constants.GRAVITY_SPEED = 4.5
        if timer >= "Time: 01:50:00":
            constants.GRAVITY_SPEED = 4.75
        if timer >= "Time: 02:00:00":
            constants.GRAVITY_SPEED = 5