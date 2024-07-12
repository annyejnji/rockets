from time import sleep
from tuke_openlab.lights import Color 

class Healthpoints:
    def __init__(self, lights):
        self.color = Color(r=255)
        self.hp_list = [light for light in range(82,98)]
        self.lights = lights

        self.lights.set_same_color(self.hp_list, Color(g=255), 1500)
    
    def lose_life(self):
        a = self.hp_list.pop()
        b = self.hp_list.pop()
        self.lights.set_same_color([a,b], Color(), 1500)

    def lost(self):
        hp_lights = [light for light in range(82,98)]
        for _ in range(3):
            self.lights.set_same_color(hp_lights, Color(r=255), 1500)
            sleep(0.1)
            self.lights.set_same_color(hp_lights, Color(), 1500)
            sleep(0.2)