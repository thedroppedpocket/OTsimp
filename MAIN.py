import random
import time
from PROFILE import Profile
from CART import Cart
from SHOP import *
from MENU import *
from HUNTING import *
from EVENTS import *
from HIGHSCORES import *
from failscrn import *
from winscrn import *

def returnKey():
    flag = True
    while (flag == True):
        key = str(input("Press enter to return to previous menu:"))
        if (key == ""):
            flag = False
            print("returning...\n\n")
            time.sleep(1)
def grtScrn():
    flag = True
    while flag == True:
        try:
            grtscrnfile = open("grtscrn.txt","r")
            for line in grtscrnfile:
                print(line)
            grtscrnfile.close()
            selectionIsGood = False
            while selectionIsGood == False:
                menuInput = int(input("Selection:"))
                selectionIsGood = True
                if menuInput == 1:
                    highscore1file = open("highscoresE.txt","r")
                    print("\n\nThe highscores for banker are:")
                    for HS1line in highscore1file:
                        print(HS1line)
                    highscore2file = open("highscoresH.txt","r")
                    print("\nThe highscores for carpenter are:")
                    for HS2line in highscore2file:
                        print(HS2line)
                    returnKey()
                elif menuInput == 2:
                    flag = False
                else:
                    print("The number you entered seems to not be on the menu...\nPlease enter one of the menu choices.")
                    selectionIsGood = False
        except FileNotFoundError:
            print("You are missing a file from oregon trail, please re-download the folder")
        except ValueError:
            print("You have entered an input that is not a number")


def typePerson(Player):
    selectionIsGood = False
    while selectionIsGood == False:
        try:
            print("You may play as one of two characters.\n1. A banker - starts with more money.\n2. A carpenter - starts with less money.")
        
            menuInput = int(input("selection:"))
            selectionIsGood = True
            if menuInput == 1:
                Player.setMoney(2000)
                Player.setDifficulty(1)
                print("\nYOU HAVE CHOSEN BANKER.")
            elif menuInput == 2:
                Player.setMoney(1000)
                Player.setDifficulty(2)
                print("\nYOU HAVE CHOSEN CARPENTER. GOODLUCK!")
            else:
                print("The number you entered seems to not be on the menu...\nPlease enter one of the menu choices.")
                selectionIsGood = False
        except ValueError:
            print("\n\nYou have entered an input that is not a number\n\n")

def distanceToDest(Player):
	distanceToDest = 400 - Player.getDistance()
	print("Distance Left:", distanceToDest,"miles.")


def main():
    grtScrn()
    Player = Profile()
    typePerson(Player)
    print("You will start with $",Player.getMoney())
    print("\n\nNow you will enter your player names.\nRemember, your leading character name will be stored as your highscore name at\nthe end of the game.\n")
    Player.setNames()
    print("\n\nWELCOME TO THE SHOP:\nBefore you start your journey you should stock up on some supplies.\n\n")
    shop(Player)
    enterMenu(Player)
    while (Player.getHealth()>0) and (Player.getDistance()<400):
        print("\n\n****NEW DAY****")
        print("\n\nYou have been traveling for", Player.getDay() ,"days.")
        Player.foodDayCounter()
        print("You have", Player.getFood(),"pounds of food left.")
        Player.distanceCounter()
        distanceToDest(Player)
        events(Player)
        death(Player)
        key = str(input("\n\nPress any key to pause game.\nPress enter to continue to next day:"))
        if (key == ""):
            print("Continuing to the next day...\n\n")
            time.sleep(1)
        else:
            enterMenu(Player)
        if (Player.getHealth()<1):
            failscrn()
            returnKey()
        elif (Player.getDistance()>=400):
            winscrn()
            if Player.getDifficulty()== 1:
                highScoresE(Player)
            elif Player.getDifficulty() == 2:
                highScoresH(Player)
            returnKey()
main()
