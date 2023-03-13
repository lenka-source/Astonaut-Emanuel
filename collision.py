import pygame
import math

def is_collision(discPosition, player_x, player_y):
    distance = math.sqrt ((math.pow(discPosition[0] - player_x, 2)) + (math.pow(discPosition[1] - (player_y+26), 2)))
    if distance < 90:
        return True
    else:
        return False