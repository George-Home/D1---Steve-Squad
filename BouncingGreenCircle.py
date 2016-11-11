import pygame
import pygame.locals

pygame.init()
done=0
clock=pygame.time.Clock()


#current position
circle_x=250
circle_y=400

#changing position of the circle
circle_change_x=2
circle_change_y=2

#Moving speed
circle_x+=1
circle_y+=1

while done == False:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
    
#Screen Window
    screen_width=700
    screen_height=700
    screen= pygame.display.set_mode((screen_width,screen_height))

    #circle - circle(Surface, color, pos, x, y, width, height)
    pygame.draw.circle(screen,(0,255,0),(circle_x,circle_y),60,60)

#Bounce circle
    if circle_x>640 or circle_x<60:
        circle_change_x*=-1
    if circle_y>640 or circle_y<60:
        circle_change_y*=-1

    circle_x+=circle_change_x
    circle_y+=circle_change_y 
 
#Display and speed
    pygame.display.flip()
    clock.tick(180)



    
#http://programarcadegames.com/index.php?chapter=introduction_to_animation&lang=en#section_8
