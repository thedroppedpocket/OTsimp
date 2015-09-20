import time
import random
def hunting(Player):
    if Player.getAmmo()< 10:
        print("You cannot hunt without ammo. sorry...")
        time.sleep(1)
        return
    else:
        Player.setAmmo(Player.getAmmo() - 10)
        
        guessNum = 0
        num = random.randint(0,10)
        flag = True
        while (flag == True) and (guessNum<3):
            try:
                if (guessNum == 0):
                    guess = int(input("Please guess a number between 0 and 10:"))
                guessNum += 1
                if (guess<num):
                    print("number is too small")
                    
                elif(guess>num):
                    print ("number is too big")
                    
                else:
                    print("great! you guessed right!")
                    Player.setFood(Player.getFood()+100)
                    print("You have received 100 pounds of food!")
                    flag = False
                if (0<guessNum<3) and (flag != False):
                    guess = int(input("Please guess another number:"))
            except(ValueError):
                print("You have entered a letter instead of a number.\ntry again.")
        if (guessNum > 3):
            print("Oh No! you ran out of guesses! try hunting again later.")

