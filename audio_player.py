from pygame import mixer

class AudioPlayer():

    def __init__(self):
        self.game_music = mixer.Sound("./sounds/game_music.wav")
        self.game_over = mixer.Sound("./sounds/game_over.wav")

        self.lose_life = mixer.Sound("./sounds/lose_life.wav")
        self.collision = mixer.Sound("./sounds/collision.wav")
       

        self.gain_life =mixer.Sound("./sounds/gain_life.wav")
        self.gain_gun = mixer.Sound("./sounds/gain_gun.wav")
        self.shoot =mixer.Sound("./sounds/shoot.wav")
        self.enemy_enemy_collision =mixer.Sound("./sounds/enemy_enemy_collision.wav")

        
    def play_collision(self):
        self.collision.play()
    
    def play_game_over(self):
        self.game_over.play()

    def play_lose_life(self):
        self.lose_life.play()

    def play_game_music(self):
        self.game_music.play()
