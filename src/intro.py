import pygame
import time, random
def draw_intro_screen(screen, game):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height() 

    intro_image = pygame.image.load("assets/images/intro.jpg")
    intro_image = pygame.transform.scale(intro_image, (WIDTH,HEIGHT))
    screen.blit(intro_image, (0, 0))
    pygame.display.flip()
    time.sleep(2)
    return "menu"
    