import pygame
import time
import random

def kishan() :
    # initialize pygame
            pygame.init()
            #set window dimensions
            display_width = 800
            display_height = 600
            
            #define colours
            black = (0,0,0)
            white = (255,255,255)
            red = (255,0,0)
            
            tank_width = 73
            
            gameDisplay = pygame.display.set_mode((display_width,display_height))
            pygame.display.set_caption('TANK')
            clock = pygame.time.Clock()
            
            # Importing the Tank image
            tankImg = pygame.image.load('data/tank.png')
            
            #######
            def things(thingx, thingy, thingw, thingh):
                oTank = pygame.image.load('data/tank.png')
                gameDisplay.blit(oTank,(thingx, thingy, thingw, thingh)) #copies pixels from tank image to gameDisplay to display to the screen
            #######
            
            
            # Generates a random letter from the given set
            randv = random.choice('ad')    
            
            #copies pixels from tank image to gameDisplay to display to the screen
            def tank(x,y):
                gameDisplay.blit(tankImg,(x,y))
            
            
            # Text output data, font, size etc. 
            def text_objects(text, font):
                textSurface = font.render(text, True, black)
                return textSurface, textSurface.get_rect()
            
            #function for display the text or message to the user
            def message_display(text):
                largeText = pygame.font.Font('freesansbold.ttf',115)
                TextSurf, TextRect = text_objects(text, largeText)
                TextRect.center = ((display_width/2),(display_height/2))
                gameDisplay.blit(TextSurf, TextRect)
            
            
            #updates the display
                pygame.display.update()
            
            #stops everything for two seconds 
                time.sleep(2)
            
            #calls the game loop function that is defined below
                game_loop()
                
                
            #crash function which is called when the tank crashes and displays text using the message_display function
            def crash():
                message_display('You Crashed')
                
            #defines the game loop and the x and y position of the tanks
            def game_loop():
                x = (display_width * 0.45)
                y = (display_height * 0.8)
            
                x_change = 0
                y_change = 0
            
            
            
            
                
            ###### The random tank generation within the game display with all its data
                thing_startx = random.randrange(50, display_width)
                thing_starty = -300
                thing_speed = 5
                thing_width = 50
                thing_height = 100
            ######
            
            ## Main game logic
            
            
            
            
                gameExit = False
            
                while not gameExit:
            
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            quit()
            
                        #print random value to the console
                        print(randv)
                        
                        #gets the value from the random generation and moves the tank based on that key
                        #if event.type == pygame.USEREVENT:
                        if randv == 'a':
                           x_change = -5
                        if randv == 'd':
                           x_change = 5
                        if randv == 'w':
                           y_change = -5
                        if randv == 's':
                           y_change = 5
                      
            
                    #adds or subtracts the value of the x/y varible so that the tank moves
                    x += x_change
                    y += y_change
                    gameDisplay.fill(white)
            
                 ########## generates a random tank and moves it down from the screen 
                    # things(thingx, thingy, thingw, thingh, color)
                    things(thing_startx, thing_starty, thing_width, thing_height)
                    thing_starty += thing_speed
                    tank(x,y)
                 ##########
            
                    
                    
                    #checks if the tanks have crashed
                    if x > display_width - tank_width or x < 0:
                        crash()
            
            
                    # chooses a random x location 
                    if thing_starty > display_height:
                        thing_starty = 0 - thing_height
                        thing_startx = random.randrange(0,display_width)
            
                    if y < thing_starty+thing_height:
                        #print('y crossover')
            
                        if x > thing_startx and x < thing_startx + thing_width or x+tank_width > thing_startx and x + tank_width < thing_startx+thing_width:
                            #print('x crossover')
                            crash()
                    
                    pygame.display.update()
                    clock.tick(60)
            ## End main game logic
            game_loop()
            
                    
            pygame.quit()
            quit()
