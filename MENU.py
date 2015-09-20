import time
import random
from HUNTING import *
def returnKey():
    flag = True
    while (flag == True):
        key = str(input("Press enter to return to previous menu:"))
        if (key == ""):
            flag = False
            print("returning...\n\n")
            time.sleep(1)

def showSupplies(Player):
    print("* * *Supplies* * *")
    print("Food:\t" , Player.getFood())     
    print("Ammunition:\t" , Player.getAmmo())
    returnKey()
    
def paceMenu(Player):
    flag = True
    while (flag == True):
        try:
            print("* * *Pace* * *")
            print("1. Casual:\t You are more cautious in your travels, but sacrifice speed as a result.")
            print("2. Strenuous:\t You move at a faster rate, but the travel is harder on your group.")
            print("3. Cruel:\t Coax out of your party as much speed as possible. Not approved by the Humane Society.")
            selection = int(input("Enter your selection: "))
            if(selection == 1):
                Player.setPace(10)
                flag = False
                
            elif(selection == 2):
                Player.setPace(15)
                flag = False
                
            elif(selection == 3):
                Player.setPace(20)
                flag = False
            else:
                print("Your choice is not on the list, try again. ")
                
        except ValueError:
            print("Invalid choice, try again.")
        returnKey()

def rationMenu(Player):
    flag = True
    while (flag == True):
        try:
            print("* * *Rations* * *")
            print("1. Filling:\t Meals are large and keep your party happy.")
            print("2. Sparse:\t Keeps your stores higher, but makes the travel harder for the group.")
            print("3. Basic:\t Meals are barely enough to keep from starvation.")
            selection = int(input("Enter your selection: "))
            if(selection == 1):
                Player.setRation(4)
                flag = False
                
            elif(selection == 2):
                Player.setRation(2)
                flag = False
            
            elif(selection == 3):
                Player.setRation(1)
                flag = False

            else:
                print("Your choice is not on the list, try again. ")
            if Player.getFood() == 0:
                Player.setRation(1)
                
        except ValueError:
            print("Invalid choice, try again.")
    returnKey()
def rest(Player):
    flag = True
    while (flag == True):
        try:
            print("* * *Rest* * *")
            rest = int(input("How many days would you like to rest?: "))
            for x in range(rest):
               Player.foodDayCounter()
               Player.setHealth(Player.getHealth() + random.randint(2,5))
               flag = False
                
        except ValueError:
            print("Invalid choice, try again.")

    returnKey()
def enterMenu(Player):  
    paused = True
    while(paused == True):
        try:
            choice = 0
            print("\n\n* * * *Paused* * * *\n\n")
            print("STATS:\n")
            print("Day" , Player.getDay())
            print("Rations:" , (Player.getRation() * len(Player.getNames())) , "pounds per day")
            print("Pace:" , Player.getPace() , "miles per day")
            print("Health:" , Player.getHealth())
            print("\n\n")
            print("1. Continue journey\n2. Show supplies\n3. Change pace")
            print("4. Food rationing\n5. Rest\n6. Hunt for food\n")
            choice = int(input("Enter your selection: "))
            if(choice == 1):
                print("Return to game.")
                paused = False
            elif(choice == 2):
                showSupplies(Player)
            elif(choice == 3):
                paceSet = paceMenu(Player)
            elif(choice == 4):
                rationset = rationMenu(Player)
            elif(choice == 5):
                rest(Player)
            elif(choice == 6):
                print("* * *Hunting* * *")
                print("To hunt, you will have 3 guesses to find the correct number between 0 and 10 inclusive. If you succeed, you will receive 100 food.")
                hunting(Player)
                Player.foodDayCounter()
            else:
                  print("What you entered was not valid. Please try again")

        except ValueError:
            print("Invalid choice, try again.")


