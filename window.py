import pygame
import os 

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen_width = 1280
screen_height = 720

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Astronaut Emanuel')
