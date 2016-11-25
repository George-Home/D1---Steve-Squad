import pygame
import time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
#For testing purposes
width = 800
height  = 600
#------------
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('Tank Game')



time = pygame.time.Clock()

block_size = 10
FPS = 30

font = pygame.font.SysFont(None, 25)
#function for printing out the gameover message
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [width/2, height/2])

#Used to be called "Start" but for teamwork purposes, it had to be changed.
#Starts with a 'dot' in the middle of the screen and while the game is not ended (while use is not pressing "q")
#the game runs.
def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = width/2
    lead_y = height/2

    lead_x_change = 0
    lead_y_change = 0

    while not gameExit:
#when game is over, it prints a message telling the user either to press C to restart the game or Q to quit 
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
#Did this for testing issues. Also, random movements weren't my part.
#Movements are based on arrow key press

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
#Game is over when the tank hits the border of the gamescreen(still for testing purpose)
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,block_size,block_size])
        pygame.display.update()

        time.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
