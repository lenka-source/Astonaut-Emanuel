import pygame
import random
from medium import Medium
from window import screen
from collision import is_collision
from player import Player
from background import Background
import sys

pygame.init()

# Sounds and backgound music
#music = pygame.mixer.music.load('sounds/music.mp3')
#pygame.mixer.music.play(-1)
disc_sound = pygame.mixer.Sound('sounds/disc.WAV')
explosion_sound = pygame.mixer.Sound('sounds/explosion.WAV')
finish_sound = pygame.mixer.Sound('sounds/finish.wav')

# Class Player -> (X, Y, width, height)
player = Player(64,300, 64, 64)
background = Background()

# Disk score
disc_taken = 0

# Time
start_ticks=pygame.time.get_ticks()

class Level_1():
    def __init__(self):
        self.disc_picture = pygame.image.load('images/disc.png')
        self.list_of_discs = []
        self.number_of_discs = 20
        
        self.asteroid_picture = pygame.image.load('images/asteroid.png')
        self.list_of_asteroids = []
        self.number_of_asteroids = 10
        
        self.explosion_picture = pygame.image.load('images/explosion.png')
        self.exploded_positions = []
        
        self.comet_picture = pygame.image.load('images/comet.png')
        self.list_1 = []
        self.number_of_comets = 10

    # Discs
    def create_discs(self):
        for i in range(self.number_of_discs):
            self.list_of_discs.append(Medium(self.disc_picture, (random.randint(430,5500),random.randint(50,670)))) 
            
    def draw_disc(self, disc):
        screen.blit(disc.picture, disc.position)    

    def collision(self, disc, i): 
        global disc_taken
        if is_collision(disc, player.player_x, player.player_y):
            self.list_of_discs.pop(i)
            disc_sound.play()
            disc_taken += 1

    def move(self, keys, disc):
        if ((player.player_x > 576) and (keys[pygame.K_RIGHT])):
            disc.position = (disc.position[0]-2, disc.position[1])

    # Asteroids
    def create_asteroids_2(self):
        if random.randint(0, 5000) < 20:
            print('asteroid generated!')
            self.number_of_asteroids = self.number_of_asteroids + 1
            self.list_of_asteroids.append(Medium(self.asteroid_picture, (random.randint(player.player_x + screen.get_width() + 200,5000),random.randint(50,670))))
            #random.randint(player.player_x, 5000)
    # Asteroids
    def create_asteroids(self):
         for i in range(self.number_of_asteroids):
            self.list_of_asteroids.append(Medium(self.asteroid_picture, (random.randint(430,5000),random.randint(50,670))))
            #instance = Medium.__init__(self.asteroid_picture, (random.randint(430,5000),random.randint(50,670)))
    def draw_asteroid(self, asteroid): 
        screen.blit(asteroid.picture, asteroid.position)

    def collision_asteroid(self, asteroid_position, i):
        if is_collision(asteroid_position, player.player_x, player.player_y):
            self.exploded_positions.append(((player.player_x,player.player_y), asteroid_position))
            self.list_of_asteroids.pop(i)

    def move_asteroid(self, asteroid, isScrolling):
        if (isScrolling):
            asteroid.position = (asteroid.position[0] -4, asteroid.position[1])
        else:
            asteroid.position = (asteroid.position[0] -2, asteroid.position[1])

    # Komets
    def create_comets(self):
        for i in range (self.number_of_comets):
            self.list_1.append(Medium(self.comet_picture, (random.randint(430,5000),random.randint(50,670))))

    def draw_comets(self, comet): 
        screen.blit(comet.picture, comet.position)

    def move_comet(self, comet, isScrolling):
        if (isScrolling):
            comet.position = (comet.position[0] -4, comet.position[1] +4)
        else:
            comet.position = (comet.position[0] -2, comet.position[1] +2)

    # Loop >>>
    def maintain_loop(self, keys, isScrolling):
    
        # Disk score
        font = pygame.font.Font(None, 50)
        disc_text = font.render('Disks: ' + str(disc_taken), 1, (255, 255, 255))
        screen.blit(disc_text, (10,10))
        
        # Time
        seconds = (pygame.time.get_ticks()-start_ticks)/1000
        time_text = font.render('Time: ' + str(seconds), 1, (255, 255, 255))
        screen.blit(time_text, (10,50))

        #Random
        self.create_asteroids_2()

        self.number_of_discs = len(self.list_of_discs)
        for i in range(len(self.list_of_discs)):
            offset_1 = self.number_of_discs-len(self.list_of_discs)
            current_disc = self.list_of_discs[i-offset_1]
            self.draw_disc(current_disc)
            self.move(keys, current_disc)
            self.collision(current_disc.position, i-offset_1)
        self.number_of_asteroids = len(self.list_of_asteroids)
        for i in range(len(self.list_of_asteroids)):
            offset_2 = self.number_of_asteroids-len(self.list_of_asteroids)
            current_asteroid = self.list_of_asteroids[i-offset_2]
            self.draw_asteroid(current_asteroid)
            self.move_asteroid(current_asteroid, isScrolling)
            self.collision_asteroid(current_asteroid.position, i-offset_2)
        if (len(self.exploded_positions)):
            for i in range (len(self.exploded_positions)):
                current_exploded_position = self.exploded_positions[i]
                player_position = current_exploded_position[0]
                asteroid_position = current_exploded_position[1]
                screen.blit(self.explosion_picture, ((player_position[0] + asteroid_position[0])/2,  (player_position[1] + asteroid_position[1])/2))
            pygame.display.update()
            explosion_sound.play()
            pygame.time.wait(1000)
            #player.player_x = 64
            #player.player_y = 300
            self.exploded_positions = []
        
        for i in range(len(self.list_1)):
            offset_3 = self.number_of_comets-len(self.list_1)
            current_comet = self.list_1[i-offset_3]
            self.draw_comets(current_comet)
            self.move_comet(current_comet, isScrolling)

        # Finish >>>
        if background.scrolled == 2999:
            
            # Disk score
            font_2 = pygame.font.Font(None, 100)
            
            disc_text_2 = font_2.render('Disks taken: ' + str(disc_taken), 1, (255, 255, 255))
            screen.blit(disc_text_2, (400,300))
        
            # Time
            time_text_2 = font_2.render('Your time: ' + str(seconds), 1, (255, 255, 255))
            screen.blit(time_text_2, (400,400))
            
            pygame.display.update()
            
            finish_sound.play()

            pygame.time.wait(3000)
            background.scrolled += 1
            sys.exit()
            
