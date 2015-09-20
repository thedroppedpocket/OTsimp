from EVENTS import *

class Profile:
    #constructor
    def __init__(self):
        self.names = ["John","Paul","George","Ringo", "Pete"]
        self.food = int(0)
        self.ammo = int(0)
        self.difficulty = int(1)
        self.health = int(100)
        self.day = int(1)
        self.ration = int(4)
        self.distance = int(0)
        self.pace = int(10)
        self.money = int(0)
        self.dead = int(0)
        

    #accessors
    def getNames(self): return self.names
    def getFood(self): return self.food
    def getAmmo(self): return self.ammo
    def getDifficulty(self): return self.difficulty
    def getHealth(self): return self.health
    def getDay(self): return self.day
    def getRation(self): return self.ration
    def getDistance(self): return self.distance
    def getPace(self): return self.pace
    def getMoney(self): return self.money
    def getDead(self): return self.dead

    #mutators
    def setNames(self):
        self.names[0] = str(input("Please enter the name of your leading character:"))
        self.names[1] = str(input("Please enter the name of your second character:"))
        self.names[2] = str(input("Please enter the name of your third character:"))
        self.names[3] = str(input("Please enter the name of your fourth character:"))
        self.names[4] = str(input("Please enter the name of your fifth character:"))
    def setFood(self, newFood): self.food = newFood
    def setAmmo(self, newAmmo): self.ammo = newAmmo
    def setDifficulty(self, newDifficulty): self.difficulty = newDifficulty
    def setHealth(self, newHealth): self.health = newHealth
    def setDay(self, newDay): self.day = newDay
    def setRation(self, newRation): self.ration = newRation
    def setDistance(self, newDistance): self.distance = newDistance
    def setPace(self, newPace): self.pace = newPace
    def setMoney(self, newMoney): self.money = newMoney
    def setDead(self, newDead): self.dead = newDead

    #other functions
    def numPeople(self):
        peopleLeft=0
        for element in (self.getNames()):
            peopleLeft += 1
        return peopleLeft
    
    def foodDayCounter(self):
        self.setFood(self.getFood()-(self.getRation() * self.numPeople()))
        self.setDay(self.getDay()+1)
        if self.getFood() <= 0:
            self.setFood(0)
            self.setHealth(self.getHealth()-10)
            print("If you don't buy food or hunt, people will start eating eachother.")
            print("Your health is now:",self.getHealth())
        
    def distanceCounter(self):	
        self.setDistance(self.getDistance()+self.getPace())
    def skipDays(self, numDaySkip):
        for i in range(numDaySkip):
            self.foodDayCounter()
            death(self)
            
        
