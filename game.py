import sys
import random
from time import sleep
import tuke_openlab
from tuke_openlab.environment import Environment

import pygame
#from audio_player import AudioPlayer
from player import Player
#from shooter import Shooter
from life import Life
from player_bullet import PlayerBullet
from enemy_bullet import EnemyBullet
from healthpoints import Healthpoints



class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_mode((100,100))
        pygame.display.set_caption("Vajcovka")
        # environment = Environment("openlab.kpi.fei.tuke.sk", 1883, is_tls=False, simulation_topic="ls861mi")
        environment = Environment("openlab.kpi.fei.tuke.sk", 1883, is_tls=False)
        self.openlab = tuke_openlab.Controller(environment)

        # self.openlab = tuke_openlab.Controller(tuke_openlab.simulation_env("ls861mi"))
        # self.openlab = tuke_openlab.Controller(tuke_openlab.production_env())
        self.clock = pygame.time.Clock()
        #self.audio_player = AudioPlayer()
        # sleep(5)
        self.run = True

        def on_recognized(data):
            # print(data)
            commands = data.split(' ')
 
            for command in commands:
                command = command.lower()
                print(f"voice command: {command}")
                #print(f"position pred: {self.player.position}")
                if command == "doľava" or command =="vľavo" or command =="trnava" or command =="orava" or command == "ľavá" or command == "dovala" or command == "zľava" or command == "javo" or command == "lavo" or command == "zdravo" or command == "gabo" or command == "viamo":
                    if self.player.position > 27:
                        self.player.move_right()
                        self.shot()
                elif command == "doprava" or command == "dobrá" or command == "správa" or command == "právo" or command == "tabu" or command == "stalo":
                    if self.player.position < 70:
                        self.player.move_left()  
                        self.shot()
                elif command == "hore":
                    self.shot()
                #print(f"position po: {self.player.position}") 
                

        self.openlab.voice_recognition.on_recognized(on_recognized) 

        def on_movement(data):
            print("movement: {data}")

        self.openlab.kinect.turn_on()
        self.openlab.kinect.on_movement(on_movement)
        # self.openlab.movement_tracker.turn_on()
        # self.openlab.movement_tracker.on_movement(on_movement)
    
    def turn_off_everything(self):
        self.openlab.lights.turn_off()

    def reinitialize_enemy_bullet(self):
        self.enemy_bullet.destroy()
        self.enemy_bullet = EnemyBullet(random.choice((1,28,55)), self.openlab.lights)
    
    def reinitialize_player_bullets(self):
        for player_bullet in self.player_bullets:
            player_bullet.destroy()
        self.player_bullets = []

    def main(self):
        self.turn_off_everything()
        self.player = Player(self.openlab.lights)
        # self.shooter = Shooter (self.openlab.lights)
        self.life = Life (self.openlab.lights)
        self.enemy_bullet = EnemyBullet(random.choice((1,28,55)), self.openlab.lights)
        self.player_bullets = []
        self.healthpoints = Healthpoints(self.openlab.lights)
        #self.audio_player.play_game_music()
        
        while self.run:
            #self.handle_input()
            self.handle_borders()

            self.enemy_bullet.update()
            
            for bullet in self.player_bullets:
                bullet.update()

            self.handle_collision()
            self.clock.tick(1)
            pygame.display.update()
            sleep(0.08)
        self.openlab.kinect.turn_off()

    def shot(self):
        position = self.player.position-1
        player_bullet = PlayerBullet(position, self.openlab.lights)
        self.player_bullets.append(player_bullet)

    #def handle_input(self):
        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
             #   self.exit_game()

            #if event.type == pygame.KEYDOWN:
                #if event.key == pygame.K_LEFT:
                #    if self.player.position > 27:
                #        self.player.move_right()
                #if event.key == pygame.K_RIGHT:
                #    if self.player.position < 70:
                #        self.player.move_left()  
                #if event.key == pygame.K_UP:
                    #self.shot()
                #sif event.key == pygame.K_w:
                    #sif self.shooter.position != 1 or self.shooter.position != 28 or self.shooter.position != 55:
                      #sself.shooter.move_forward()
                #sif event.key == pygame.K_s:
                  #  if self.shooter.position % 27 != 0 or self.shooter.position % 26 != 0 or self.shooter.position % 25 != 0:
                    #    self.shooter.move_backward()
                #if event.key == pygame.K_a:
                 #   if self.shooter.position > 27:
                  #      self.shooter.move_right()
                #if event.key == pygame.K_d:
                 #   if self.shooter.position < 70:
                 #       self.shooter.move_left()  

    def handle_collision(self):
        def intersects(a, b):
            return len(set(a) & set(b)) > 0

        if intersects([self.player.position - 1], self.enemy_bullet.path):
            self.healthpoints.lose_life()
            #self.audio_player.play_lose_life()

            if len(self.healthpoints.hp_list) <= 0:
                self.healthpoints.lost()
                #self.audio_player.play_game_over()
                self.turn_off_everything()
                self.run = False
            else:
                self.reinitialize_enemy_bullet()
                self.reinitialize_player_bullets()
            return
            
        #if intersects([self.shooter.position - 1], self.enemy_bullet.path):
            #self.reinitialize_enemy_bullet()
            #self.reinitialize_player_bullets()
            #return
        
        for player_bullet in self.player_bullets:
            if intersects(player_bullet.path, self.enemy_bullet.path):
                #self.audio_player.play_collision()
                self.reinitialize_enemy_bullet()
                self.reinitialize_player_bullets()
                break


    def handle_borders(self):
        removed_player_bullets = []
        for player_bullet in self.player_bullets:
            if (player_bullet.position + 26) % 27 == 0:
                player_bullet.destroy()
                removed_player_bullets.append(player_bullet)
        
        for player_bullet in removed_player_bullets:
            self.player_bullets.remove(player_bullet)

        if self.enemy_bullet.position % 27 == 0:
            self.healthpoints.lose_life()
            #self.audio_player.play_lose_life()

            if len(self.healthpoints.hp_list) <= 0:
                self.healthpoints.lost()
                #self.audio_player.play_game_over()
                self.turn_off_everything()
                self.run = False
            else:
                self.reinitialize_enemy_bullet()
                self.reinitialize_player_bullets()

    def exit_game(self):
        self.openlab.kinect.turn_off()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.main()