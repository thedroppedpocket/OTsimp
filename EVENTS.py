import random
def death(Player):
    people = Player.getNames()
    healthNum = int(Player.getHealth())
    
    if (healthNum <= 80) and (healthNum > 60) and (Player.getDead() == 0):
        print(people[-1],"has died.")
        people.remove(people[-1])
        print("People Left:")
        Player.setDead(Player.getDead() + 1)
        for x in people:
            print(x)
     
    elif (40<Player.getHealth() <= 60) and (Player.getDead() == 1):
        print(people[-1],"has died.")
        people.remove(people[-1])
        print("People Left:")
        Player.setDead(Player.getDead() + 1)
        for x in people:
            print(x)

    elif (20<Player.getHealth() <= 40) and (Player.getDead() == 2):
        print(people[-1],"has died.")
        people.remove(people[-1])
        print("People Left:")
        Player.setDead(Player.getDead() + 1)
        for x in people:
            print(x)

    elif (0<Player.getHealth() <= 20) and (Player.getDead() == 3):
        print(people[-1],"has died.")
        people.remove(people[-1])
        print("People Left:")
        Player.setDead(Player.getDead() + 1)
        for x in people:
            print(x)

    elif Player.getHealth() <= 0:
        print(people[-1],"has died.")
    
def events(Player):
    name = random.choice(Player.getNames())
    events = ["has exhaustion", "has a broken arm", "has a broken leg", \
            "has dysentery", "has cholera", "has typhoid", "drank bad water.", "is dehydrated."]  
    events2 = ["Broken axle.", "Missing wheel.", "Impassable trail.", "Lost trail"]
    a = random.randint(0, 3)
    b = random.randint(0, 3)
    c = random.randint(0, 4)
    d = random.randint(0, 4)
    e = random.randint(0, 10)
    f = random.randint(0, 10)
    g = random.randint(0, 24)
    h = random.randint(0, 24)
    numDaySkip = random.randint(1, 3)
    if a == b:
        print(name,random.choice(events))
        Player.setHealth(Player.getHealth() - 5)
        print("Your health is now",Player.getHealth(),".")
        
    elif c == d:
        print(random.choice(events2))
        Player.skipDays(numDaySkip)
        
        print("You lost",numDaySkip,"days.")
    elif e == f:
        print("Your wagon broke.")
        if a == b:
            print("You were able to repair it.")
        else:
            Player.skipDays(numDaySkip)
            print("You had to wait for someone to help and lost",numDaySkip," days.")
    elif g == h:
        flag = True  
        while flag == True:
            try:
                itemsList = ["food", "ammunition"]
                itemsMinusAmmo = ["food"]
                itemsMinusFood = ["ammunition"]
                inputRiver = int(input("Enter 1 to ford the river, 2 to float across, 3 to wait for conditions to wait until conditions improve."))
                if inputRiver == 1:
                    print("Attempting to ford river...")
                    a = random.randint(0, 2)
                    b = random.randint(0, 2)
                    if a == b:
                        print("Congratulations, you successfully forded the river.")
                        flag = False 	 
                    else:
                        if Player.getAmmo() == 0:
                            itemLost = random.choice(itemsMinusAmmo)
                        elif Player.getFood() == 0:
                            itemLost = random.choice(itemsMinusFood)
                        if Player.getAmmo() > 0 and Player.getFood() > 0:
                            itemLost = random.choice(itemsList)
                        if (itemLost == itemsList[0]) or (itemLost == itemsMinusFood):
                            itemsLost = random.randint(1, 300)
                            Player.setFood(Player.getFood() - itemsLost)
                            print("You forded the river, but lost",itemsLost,itemLost,". You have",Player.getFood(),itemLost,".")
                            
                        elif (itemLost == itemsList[1]) or (itemLost == itemsMinusAmmo):
                            itemsLost = random.randint(1, 60)
                            Player.setAmmo(Player.getAmmo() - itemsLost)
                            print("You forded the river, but lost",itemsLost,itemLost,". You have",Player.getAmmo(),itemLost,".")
                            flag = False
                elif inputRiver == 2:
                    
                    print("Attempting to float across river.")
                    c = random.randint(0, 1)
                    d = random.randint(0, 1)
                    if c == d:
                        print("Congratulations, you successfully floated across the river.")
                        flag = False
                        
                    else:
                        if Player.getAmmo() == 0:
                            itemLost = random.choice(itemsMinusAmmo)
                        elif Player.getFood() == 0:
                            itemLost = random.choice(itemsMinusFood)
                        if Player.getAmmo() > 0 and Player.getFood() > 0:
                            itemLost = random.choice(itemsList)
                        if (itemLost == itemsList[0]) or (itemLost == itemsMinusFood):
                            itemsLost = random.randint(1, 300)
                            Player.setFood(Player.getFood() - itemsLost)
                            print("You floated across the river, but lost",itemsLost,itemLost,". You have",Player.getFood(),itemLost,".")
                            flag = False
                            return Player.getFood()
                        elif itemLost == (itemsList[1]) or (itemLost == itemsMinusFood):
                            itemsLost = random.randint(1, 60)
                            Player.setAmmo(Player.getAmmo() - itemsLost)
                            print("You floated across the river, but lost",itemsLost,itemLost,". You have",Player.getAmmo(),itemLost,".")
                            flag = False
                            return Player.getAmmo()

                elif inputRiver == 3:
                    numDaySkip = random.randint(1, 4)
                    skipDays(numDaySkip)
                    print("You have lost",numDaySkip,"days.")
                    return numDaySkip
        
            except ValueError:
                print("Invalid.")
            except NameError:
                print("Invalid.")
                    
    else:
        print("Nothing happened today.")
