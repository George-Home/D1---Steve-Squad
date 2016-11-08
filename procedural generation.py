import pygame
import random
pygame.init()
random.seed()

def procGen(surface, color, width, height):
    """Takes the drawing surface, and the rectangle color, width and
    height. Draws the rectangle in a random location on the surface."""
    surfaceW = surface.get_width() - width
    surfaceH = surface.get_height() - height
    x = random.randint(0, surfaceW)
    y = random.randint(0, surfaceH)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, width, height))
    return x, y

