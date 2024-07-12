from tuke_openlab.lights import Color 

class Shooter:
    def __init__(self, lights):
        self.position = 44
        self.color = Color(r=128, g=255)
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

    def move_forward(self):
        previous_position = self.position
        self.position -= 1
        self.lights.set_same_color([previous_position], Color(), 500)
        self.lights.set_same_color([self.position], self.color, 500)

    def move_backward(self):
        previous_position = self.position
        self.position += 1
        self.lights.set_same_color([previous_position], Color(), 500)
        self.lights.set_same_color([self.position], self.color, 500)