import pygame
import pygame.locals

pygame.init()
done=0
clock=pygame.time.Clock()

image= pygame.image.load('spaceinvader.png')

#--------------------------------------------
                  #Variables
#--------------------------------------------
#Image Position
image_x= 400
image_y= 400

#Image moving speed
image_x_change = 2
image_y_change = 2

#moving speed
image_x+=1
image_y+=1

White=(255,255,255)

#---------------------------------------------
                    #Game Loop
#---------------------------------------------

while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    #Screen Window
    background_colour= (White)
    screen_width=1000
    screen_height=1000
    screen= pygame.display.set_mode((screen_width,screen_height))
    screen.fill(background_colour)

    
    screen.blit(image,(image_x,image_y))
    
    #Moving Image
    if image_x > 870 or image_x < 0:
        image_x_change*= -1
    if image_y > 905 or image_y < 0 :
        image_y_change *= -1

    image_x+=image_x_change
    image_y+=image_y_change

    #Display and speed
    pygame.display.flip()
    clock.tick(180)


pygame.quit()
