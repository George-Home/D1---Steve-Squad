import pygame
import pygame.locals
import random
pygame.init()
done=0
image= pygame.image.load('spaceinvader.png') #image used in program


#--------------------------------------------
                  #Variables
#--------------------------------------------
#Image Position (Random position on screen every time the image is loaded)
image_x=random.randint(0,870) 
image_y= random.randint(0,905)

#Image moving speed
image_x_change = 2
image_y_change = 2

#Colours (RGB)
White=(255,255,255)
Blue= (0,0,255)

#Screen details
background_colour= (White)
screen_width=1000
screen_height=1000

#---------------------------------------------
                    #Game Loop
#---------------------------------------------

while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

#Screen Window
    screen= pygame.display.set_mode((screen_width,screen_height))
    screen.fill(background_colour)
    screen.blit(image,(image_x,image_y)) #runs image on screen

#Moving Image
    if image_x > 870 or image_x < 0 :
        image_x_change*= -1             
            
    if image_y > 905 or image_y < 0:
        image_y_change*= -1

    image_x+=image_x_change
    image_y+=image_y_change



    #Display
    pygame.display.flip() 
    


pygame.quit()

