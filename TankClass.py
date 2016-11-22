import random
random.seed()

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
    def move(self, x, y):
        index = Tank.__locationList.index(self.location)
        if type(x)==int and type(y)==int and (x, y, 32, 32) not in Tank.__locationList: #moves the tank object
            self.location = (x, y, 32, 32)                                              #to a specified location
            Tank.__locationList[index] = self.location                                  #as long as no other
        else:                                                                           #tanks are in that
            raise TypeError("The location must be a unique pair of two integers.")      #location

    #Location List
    def getLocationList():          #Return list of location attributes for all of the tanks
        return Tank.__locationList

        
        
