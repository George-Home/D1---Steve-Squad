import pygame
import random
pygame.init()
random.seed()
import pygame.locals
from tank import kishan

rectangles = {}
class Tank:
    """A class to store information about the tanks.
    It has attributes dodge, accuracy, crit chance, crit damage, speed, armour, attack
    range, shot speed, and shot damage.
    It has methods getDodge, addDodge, subDodge, dodgeCheck, getAccuracy, addAccuracy, subAccuracy
    getCritC, addCritC, subCritC, takeDamage, move, getLocationList.
    """
    #ATTRIBUTES
    __locationList = []
      
    def __init__(self, x, y):
        if type(x)==int and type(y)==int and (x, y, 32, 32) not in Tank.__locationList:
            self.location = (x, y, 32, 32)              #Location attribute is formatted to be compatible with the pygame
            Tank.__locationList.append(self.location)   #draw rectangle function, the last 2 values of the tuple are the 
        else:                                           #tank size
            raise TypeError("The location must be a unique pair of two integers.")
        self.__dodge = 10 #dodge
        self.health = 50
        self.__accuracy = 110
        self.__critC = 10 #Critical hit chance
        self.critD = 10 #Critical hit damage Bonus
        self.speed = 10
        self.armour = 10
        self.atkRange = 100 #Attack range
        self.shotSpeed = 10
        self.damage = 10
        self.direction = 1
  
    #METHODS
  
    #Dodge
    def getDodge(self):         #return the dodge stat
        return self.__dodge
      
    def addDodge(self, num):
        if type(num)==int:
            if self.__dodge + num in range(10, 101):    #increase the dodge stat as long as the new dodge
                self.__dodge += num                     #stat is between 10 and 100
            else:
                raise ValueError("Dodge must be between 10 and 100")
        else:
            raise TypeError("Number added must be an integer")
  
    def subDodge(self, num):
        if type(num)==int:
            if self.__dodge - num in range(10, 101):    #decrease the dodge stat as long as the new dodge
                self.__dodge -= num                     #stat is between 10 and 100
            else:
                raise ValueError("Dodge must be between 10 and 100")
        else:
            raise TypeError("Number subtracted must be an integer")
  
    def dodgeCheck(self, other):
        roll = random.randint(0, other.__accuracy)  #checks the object's dodge stat against
        if roll<=self.__dodge:                      #another object's accuracy to see if
            return True                             #the object is hit
        else:
            return False
  
    #Critical hit chance
    def getCritC(self):         #return the critical hit chance stat
        return self.__critC
      
    def addCritC(self, num):
        if type(num)==int:
            if self.__critC + num in range(10, 91):    #increase the crit chance stat as long as the new dodge
                self.__critC += num                     #stat is between 10 and 90
            else:
                raise ValueError("Critical hit chance must be between 10 and 90")
        else:
            raise TypeError("Number added must be an integer")
  
    def subCritC(self, num):
        if type(num)==int:
            if self.__critC - num in range(10, 91):     #decrease the crit chance stat as long as the new dodge
                self.__critC -= num                     #stat is between 10 and 90
            else:
                raise ValueError("critical hit chance must be between 10 and 90")
        else:
            raise TypeError("Number subtracted must be an integer")
  
    #Accuracy
    def addAccuracy(self, num):         
        if type(num)==int:
            if self.__accuracy + num in range(110, 201):    #increase the accuracy stat as long as the new
                self.__accuracy += num                      #accuracy stat is between 110 and 200
            else:
                raise ValueError("Accuracy must be between 110 and 200")
        else:
            raise TypeError("Number added must be an integer")
  
    def subAccuracy(self, num):
        if type(num)==int:
            if self.__accuracy - num in range(110, 201):    #decrease the accuracy stat as long as the new
                self.__accuracy -= num                      #accuracy stat is between 110 and 200
            else:
                raise ValueError("Accuracy must be between 110 and 200")
        else:
            raise TypeError("Number subtracted must be an integer")
  
    def getAccuracy(self):      #Return accuracy stat
        return self.__accuracy
      
    #Damage
    def takeDamage(self, other):        #calculates the health loss of the object when hit by an
        roll = random.randint(0, 100)   #enemy weapon, checks for critical hits and accounts for
        damage = other.damage           #armour
        if roll<other.__critC:
            damage += other.critD
        damage -= self.armour
        if damage<=0:
            pass
        else:
            self.health -= damage
  
    #Movement
    def move(self):
        index = Tank.__locationList.index(self.location)
        if type(x)==int and type(y)==int and (x, y, 32, 32) not in Tank.__locationList: #moves the tank object
            self.location = (x, y, 32, 32)                                              #to a specified location
            Tank.__locationList[index] = self.location                                  #as long as no other
        else:                                                                           #tanks are in that
            raise TypeError("The location must be a unique pair of two integers.")      #location

        if self.direction == 1:             #Moves the Tank Left
            self.location = (-1, 0, 32, 32) #(.location(X, Y, FormatH, FormatW)
        elif self.direction == 2:           #Moves the tank Right
            self.location = (1, 0, 32, 32)
        elif self.direction == 3:           #Moves the tank Up
            self.location = (0, 1, 32, 32)
        elif self.direction == 4:           #Moves the tank Down
            self.location = (0, -1, 32, 32)

    #Location List
    def getLocationList():          #Return list of location attributes for all of the tanks
        return Tank.__locationList
  

# spawns each tank in a given position
Tank1 = Tank(30,30)
Tank2 = Tank(930,30)
Tank3 = Tank(30,730)
Tank4 = Tank(930,730)
# sets the direction of the tank
Tank1.direction = 1
Tank2.direction = 2
Tank3.direction = 3
Tank4.direction = 4

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

# opens the counter file and reads the Count number within the file
     
    Count = 0
    Count_file = open("counter.txt", "r")
    lines = Count_file.readlines()
    Count_file.close()
# adds 1 to the Count value
    lastline = int(lines.pop())
    lastline = lastline + 1
    print(lastline)
    str_lastline = str(lastline)
#appends the new Count value to the file
    Add_File = open("counter.txt", "w")
    Add_File.write(str_lastline)
    Add_File.close()
# If the Count value reaches 200 then the direction the tanks are travelling in are randomly changed
    if lastline == 200:
        Change_Direction = random.randint(1,4)
        tank1.direction = Change_Direction
        print('Yay')

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
 

        #Tank generation - places each tank on screen in a given locations and sets it RGB Colour
        pygame.draw.rect(screen, (255,0,0), Tank1.location)
        pygame.draw.rect(screen, (255,255,0), Tank2.location)
        pygame.draw.rect(screen, (0,255,255), Tank3.location)
        pygame.draw.rect(screen, (255,0,255), Tank4.location)
        
        circle_x+=circle_change_x
        circle_y+=circle_change_y 
       
              
        pygame.display.flip()
        clock.tick(180)
  
          
  
  
pygame.init()
  
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
                        kishan()
                        gameLoop() 
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
  
  
        button("play", 150,500,100,50, green, light_green, action="Play")
        # button("controls", 350,500,100,50, yellow, light_yellow, action="Controls")
        button("quit", 550,500,100,50, red, light_red, action ="Quit")
  
        
     
               


  
        pygame.display.update()
  
        clock.tick(15)
  
  
  
  
      
  
  
  
  
  
  
    pygame.quit()
    quit()
  
  
random.seed()
  
  
  
  
game_intro()
