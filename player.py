from tuke_openlab.lights import Color 

class Player:
    def __init__(self, lights):
        self.position = 43
        self.color = Color(r=255)
        self.lights = lights

        self.lights.set_same_color([self.position], self.color, 500)

    def move_left(self):
        previous_position = self.position
        self.position += 27
        self.lights.set_same_color([previous_position], Color(), 500)
        self.lights.set_same_color([self.position], self.color, 500)

    def move_right(self):
        previous_position = self.position
        self.position -= 27
        self.lights.set_same_color([previous_position], Color(), 500)
        self.lights.set_same_color([self.position], self.color, 500)