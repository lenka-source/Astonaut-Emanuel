import pygame
from window import screen
from player import Player


background = pygame.image.load('images/background.png').convert()

class Background:
    def __init__(self):
        self.scrolled = 0
        self.background_x = 0
        self.background_x2 = background.get_width()

    def draw_screen(self):
        screen.blit(background, (self.background_x, 0))
        screen.blit(background, (self.background_x2, 0))


    def scrolling(self, keys, player_x):

        if (self.isScrolling(keys, player_x)):
            self.background_x -= 2 
            self.background_x2 -= 2
            self.scrolled += 1
            if self.background_x < background.get_width() * -1: 
                self.background_x = background.get_width()
    
            if self.background_x2 < background.get_width() * -1:
                self.background_x2 = background.get_width()

    def isScrolling(self, keys, player_x):
        return ((player_x > 576) and (keys[pygame.K_RIGHT])) and not (self.scrolled > 3000)
