import pygame
import sys
import math
from window import screen, screen_width, screen_height

# Images
playerPictureStill = pygame.image.load('images/astro-still.png')
playerPictureRight =  pygame.image.load('images/astro-right.png')
playerPictureLeft =  pygame.image.load('images/astro-left.png')

class Player():

    def __init__(self, player_x, player_y, width, height):
        self.player_x = player_x
        self.player_y = player_y
        self.width = width
        self.height = height
        

    def controls(self, keys):
        if (keys[pygame.K_UP]) == True:
            self.player_y -= 5
        
        if (keys[pygame.K_DOWN]) == True:
            self.player_y += 5
           
        if (keys[pygame.K_LEFT]) == True:
            self.player_x -= 5 
           
        if (keys[pygame.K_RIGHT]) == True:
          
            self.player_x += 5

    def draw_player(self, keys):
        if ((keys[pygame.K_RIGHT]) and (keys[pygame.K_LEFT])):
            playerScaleStill = pygame.transform.scale(playerPictureStill, (self.width, self.height))
            screen.blit(playerPictureStill, (self.player_x, self.player_y))
        if (not (keys[pygame.K_RIGHT]) and not (keys[pygame.K_LEFT])):
            playerScaleStill = pygame.transform.scale(playerPictureStill, (self.width, self.height))
            screen.blit(playerPictureStill, (self.player_x, self.player_y))
        if ((keys[pygame.K_RIGHT]) and not (keys[pygame.K_LEFT])):
            playerScaleRight = pygame.transform.scale(playerPictureRight, (self.width, self.height))
            screen.blit(playerPictureRight, (self.player_x, self.player_y))  
        if ((keys[pygame.K_LEFT]) and not (keys[pygame.K_RIGHT])):
            playerScaleLeft = pygame.transform.scale(playerPictureLeft, (self.width, self.height))
            screen.blit(playerPictureLeft, (self.player_x, self.player_y))

    def set_boundaries(self):
        if (self.player_x <= 0):
            self.player_x = 0
        if (self.player_y <= 0):
            self.player_y = 0 
        if (self.player_y >= screen_height - self.height):
            self.player_y = screen_height - self.height   
        # Preserve Y position
        if (self.player_x >= screen_width - (self.width // 2)):
            self.player_x = 0 - (self.width // 2)
