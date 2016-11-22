import pygame
import random
pygame.init()
random.seed()
import pygame.locals

rectangles = {}
def gameLoop():
    def procGen(surface, width, height):
        """Takes the drawing surface, and the rectangle color, width and
        height. Draws the rectangle in a random location on the surface."""
        surfaceW = surface.get_width() - width      #Ensures the location can't be generated
        surfaceH = surface.get_height() - height    #such that the rectangle goes off the screen
        x = random.randint(0, surfaceW)
        y = random.randint(0, surfaceH)
        while (x,y) in rectangles:          #prevents two rectagnles sharing a location
            x = random.randint(0, surfaceW)
            y = random.randint(0, surfaceH)
        rectangles[len(rectangles)] = (x,y,width,height)

#Start of contributions by Dezzy
    pygame.init()
    done=0
    clock=pygame.time.Clock()
    generated = False
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
        screen_width=1000
        screen_height=800
        screen= pygame.display.set_mode((screen_width,screen_height))
    #End of contributions by Dezzy

    #generate random point for obstcle to spawn
        if generated==False:
            for i in range(5): #input of range function determines number of rectangles generated
                procGen(screen, 32, 32)
            generated=True
            
        for i in rectangles: #draws a rectangle for each location that has been generated
            pygame.draw.rect(screen, (0,255,0), rectangles[i])
         #circle - circle(Surface, color, pos, x, y, width, height)
        pygame.draw.circle(screen,(0,255,0),(circle_x,circle_y),30,30)

    #Bounce circle
        if circle_x not in range (30,970):  #little mod by Derick and Ronan
            circle_change_x*=-1
        if circle_y not in range (30,770): #same as above
            circle_change_y*=-1

        circle_x+=circle_change_x
        circle_y+=circle_change_y 
     
            
        pygame.display.flip()
        clock.tick(180)


pygame.init() #Start of Milinda's Menu

display_width = 1000
display_height = 800

gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Tanks')

#icon = pygame.image.load("tank-152362_640.png")       
#pygame.display.set_icon(icon)

white = (255,255,255)
black = (0,0,0)


red = (200,0,0)
light_red = (255,0,0)

yellow = (200,200,0)
light_yellow = (255,255,0)

green = (34,177,76)
light_green = (0,255,0)

clock = pygame.time.Clock()




tankWidth = 40
tankHeight = 20

turretWidth = 5
wheelWidth = 5

ground_height = 35





smallfont = pygame.font.SysFont("bauhaus 93", 25)
medfont = pygame.font.SysFont("bauhaus 93", 40)
largefont = pygame.font.SysFont("bauhaus 93", 85)

#img = pygame.image.load('tank-152362_640.png')
#appleimg = pygame.image.load('tank-152362_640.png')

def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def button(text, x, y, width, height, inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    #print(click)
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            elif action == "controls":
                game_controls()

            elif action == "play":
                gameLoop()

            elif action == "main":
                game_intro()
            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameLoop() #########
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        gameDisplay.fill(black)
        message_to_screen("Girls Gone Wild Russian Edition (Tanks)",white,-100,size="medium")
        message_to_screen("The objective is to chose your perks",white,-30)
        message_to_screen("Strategy is the key",white,10)
        message_to_screen("The last one stands.",white,50)
        message_to_screen("Press C to Play ",green,180)
        message_to_screen("Press Q to Quit ",red,210)


       # button("play", 150,500,100,50, green, light_green, action="Play")
       # button("controls", 350,500,100,50, yellow, light_yellow, action="Controls")
       # button("quit", 550,500,100,50, red, light_red, action ="Quit")



        pygame.display.update()

        clock.tick(15)




    






    pygame.quit()
    quit()

game_intro()
def gameLoop():
    def procGen(surface, width, height):
        """Takes the drawing surface, and the rectangle color, width and
        height. Draws the rectangle in a random location on the surface."""
        surfaceW = surface.get_width() - width      #Ensures the location can't be generated
        surfaceH = surface.get_height() - height    #such that the rectangle goes off the screen
        x = random.randint(0, surfaceW)
        y = random.randint(0, surfaceH)
        while (x,y) in rectangles:          #prevents two rectagnles sharing a location
            x = random.randint(0, surfaceW)
            y = random.randint(0, surfaceH)
        rectangles[len(rectangles)] = (x,y,width,height)

#Start of contributions by Dezzy
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
        screen_width=1000
        screen_height=800
        screen= pygame.display.set_mode((screen_width,screen_height))
    #End of contributions by Dezzy

    #generate random point for obstcle to spawn
        if generated==False:
            for i in range(5): #input of range function determines number of rectangles generated
                procGen(screen, 32, 32)
            generated=True
            
        for i in rectangles: #draws a rectangle for each location that has been generated
            pygame.draw.rect(screen, (0,255,0), rectangles[i])
         #circle - circle(Surface, color, pos, x, y, width, height)
        pygame.draw.circle(screen,(0,255,0),(circle_x,circle_y),30,30)

    #Bounce circle
        if circle_x not in range (30,970):  #little mod by Derick and Ronan
            circle_change_x*=-1
        if circle_y not in range (30,770): #same as above
            circle_change_y*=-1

        circle_x+=circle_change_x
        circle_y+=circle_change_y 
     
            
        pygame.display.flip()
        clock.tick(180)


