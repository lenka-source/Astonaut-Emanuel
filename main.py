import pygame
from window import screen
from medium import Medium
#from draw import draw, medium
#from move import move
from LEVEL_1 import Level_1, player, background

# Class Level 1
level_1 = Level_1()

# Speed Of Game
clock = pygame.time.Clock()
speed = 90

pygame.init()
           
level_1.create_discs()
level_1.create_asteroids()
level_1.create_comets()
# Game loop >>>
def game_loop():
    running = True
    while running:
        keys = pygame.key.get_pressed()
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (keys[pygame.K_ESCAPE]):
                running = False
        background.draw_screen()
        clock.tick(speed)
        background.scrolling(keys, player.player_x)
        isScrollingBool = background.isScrolling(keys, player.player_x)
        if(player.player_x > 576):
            player.player_x = 576
        player.set_boundaries()
        player.controls(keys)
        player.draw_player(keys)

        # LEVEL 1 >>>
        level_1.maintain_loop(keys, isScrollingBool)

        pygame.display.update()

game_loop()