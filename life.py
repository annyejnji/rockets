from tuke_openlab.lights import Color
from random import randrange 

class Life:
    def __init__(self, lights):
        
        self.position = 26
        while self.position == 26 or self.position == 27 or self.position ==53 or self.position==54 or self.position ==80 or self.position ==81:
            self.position = randrange(1, 81)

        self.color = Color(r=255, g=255, b=255)
        self.lights = lights

        self.lights.set_same_color([self.position], self.color, 500)