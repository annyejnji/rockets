import random
from tuke_openlab.lights import Color

class PlayerBullet:
    def __init__(self, position, lights):
        r = random.randint (0,255)
        b = random.randint (0,255)
        color = Color(r, 255, b)
        self.color = color
        self.position = position
        self.path = [position]
        self.lights = lights

        self.lights.set_same_color([self.position], self.color, 500)
    
    def update(self):
        if ((self.position + 26) % 27) != 0:
            self.position -= 1
            self.path.append(self.position)
            self.lights.set_same_color([self.position], self.color, 500)
    
    def destroy(self):
        self.lights.set_same_color(self.path, Color(), 500)