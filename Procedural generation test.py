import pygame
import random
pygame.init()
random.seed()
import pygame.locals
generated = False
rectangles = {}
def randomGen(surface, width, height):
    """Takes the drawing surface, and the rectangle width and height.
    Returns a random location within the size of the surface."""
    surfaceW = surface.get_width() - width      #Ensures the location can't be generated
    surfaceH = surface.get_height() - height    #such that the rectangle goes off the screen
    x = random.randint(0, surfaceW)
    y = random.randint(0, surfaceH)
    while (x,y) in rectangles:          #prevents two rectangles sharing a location
        x = random.randint(0, surfaceW)
        y = random.randint(0, surfaceH)
    return (x,y,width,height)

pygame.init()
done=0

while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
#Screen Window
    screen_width=1000
    screen_height=800
    screen= pygame.display.set_mode((screen_width,screen_height))

#generate random point for rectangles to spawn
    if generated==False:
        for i in range(5): #input of range function determines number of rectangles generated
            rectangles[i] = randomGen(screen, 32, 32)
        generated=True
        
    for i in rectangles: #draws a rectangle for each location that has been generated
        pygame.draw.rect(screen, (0,255,0), rectangles[i])
        
    pygame.display.flip()

