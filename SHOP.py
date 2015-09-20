import time
from CART import Cart
from PROFILE import Profile

playerCart = Cart()
def returnKey():
    flag = True
    while (flag == True):
        key = str(input("Press enter to return to previous menu:"))
        if (key == ""):
            flag = False
            print("returning...\n\n")
            time.sleep(1)

def delCart(itemsAvailable,Player):
    print("\nRemember:\nFive pounds of food is $",itemsAvailable["Food (5 pounds)"],"\n20 bullets is $",itemsAvailable["Ammunition (20 bullets)"])
    time.sleep(1)
    flag = True
    while flag == True:
        try:
            flag = False
            playerCart.displayCart()
            print("\nRemove Food \n2.Remove Ammo\n3.Return to the shop menu.")
            delInput = int(input("Please enter your selection."))
            if delInput == 1:
                print("Cost of Food  in cart: $",playerCart.getCostFood(),"")
                playerCart.setFoodInCart(playerCart.getFoodInCart() - int(input("Please input the amount of food you wish to remove from your cart.")))
                print("Cost of Food remaining in cart: $",playerCart.getCostFood(),"\n")
            elif delInput == 2:
                print("Cost of Ammunition in cart: $",player.getCostAmmo(),"")
                playerCart.setAmmoInCart(playerCart.getAmmoInCart() - int(input("Please input the amount of ammunition you wish to remove from your cart.")))
                print("Cost of Ammunition remaining in cart: $",player.getCostAmmo(),"\n")
            elif delInput == 4:
                print("returning to shop menu...")
                time.sleep(1)
            else:
                print("You seem to have entered a number that was not in the menu. Please try again.")
                flag = True
        except ValueError:
                print("\n\nInvalid. try to put in a real number please.\n\n")
                flag = True
        
def buyFood(itemsAvailable):
    flag = True
    while flag == True:  
        try:
            flag = False
            print("Five pounds of food is $",itemsAvailable["Food (5 pounds)"],)
            playerCart.setFoodInCart(int(input("Please input the amount of food you wish to buy.")))
            print("Cost of Food in cart: $",playerCart.getCostFood(),"")
        except ValueError:
                print("\n\nInvalid.\ntry to put in a real number please.\n\n")
                flag = True
                
def buyWagon(itemsAvailable):
            playerCart.setWagonInCart(1)
            print("Cost of Wagon and Oxen in cart: $",playerCart.getCostWagon(),"")
        

def buyAmmo(itemsAvailable):
    flag = True
    while flag == True:  
        try:
            flag = False
            print("20 bullets is $",itemsAvailable["Ammunition (20 bullets)"],)
            playerCart.setAmmoInCart(int(input("Please input the amount of ammunition you wish to buy.")))
            print("Cost of Ammunition in cart: $",playerCart.getCostAmmo(),"")
        except ValueError:
                print("\n\nInvalid.\ntry to put in a real number please.\n\n")
                flag = True

def shop(Player):
    itemsAvailable = {"Food (5 pounds)" : int("1"), "Wagon and Oxen" : int("300"), "Ammunition (20 bullets)" : int("2")}
    flag = True
    while (flag == True):
        try:
            print("1. Food (5 pounds): $1\n2. Wagon and Oxen (max. 1): $300\n3. Ammunition (20 bullets): $2")
            print("4. Remove an item from your cart.")
            print("5. Leave shop and continue to trail.")
            inputShop = int(input("Input the number of your desired choice: "))
            if inputShop == 1:
                buyFood(itemsAvailable)
                print("\nFood added to cart.")
                playerCart.displayCart()
                print("You have $",(Player.getMoney() - playerCart.getTotalCost()),"remaining")
                returnKey()
                

            elif inputShop == 2:
                buyWagon(itemsAvailable)
                print("\nWagon added to cart.")
                playerCart.displayCart()
                print("You have $",Player.getMoney() - playerCart.getTotalCost(),"remaining")
                returnKey()

            elif inputShop == 3:
                buyAmmo(itemsAvailable)
                print("\nAmmo added to cart.")
                playerCart.displayCart()
                print("You have $",Player.getMoney() - playerCart.getTotalCost(),"remaining")
                returnKey()

            elif inputShop == 4:
                delCart(itemsAvailable, Player)
                playerCart.displayCart()
                print("You have $",Player.getMoney() - playerCart.getTotalCost(),"remaining")
                
            elif inputShop == 5:
                
                print("Total:" ,playerCart.getTotalCost())
                print("You have:",Player.getMoney())
                flag2 = True
                while flag2 == True:
                    try:
                        flag2 = False
                        confirmPurchase = int(input("Confirm purchase? 1 for yes, 0 for no:"))
                        if confirmPurchase == 1:
                            purchaseConfirmed = True
                        elif confirmPurchase == 0:
                            purchaseConfirmed = False
                        else:
                            print("Invalid input. Must be either 1 or 0.")
                            flag2 = True
                    except ValueError:
                        print("\nInvalid - try to put in a real number please.\n\n")
                        flag2 = True
                
            
                if Player.getMoney() < playerCart.getTotalCost():
                    print("Not enough money to complete purchase.")
                    purchaseConfirmed = False
                    
                if purchaseConfirmed == True:
                    if (playerCart.getWagonInCart() < 1):
                        print("\nYou must buy a wagon.\n")
                    else:
                        Player.setMoney(Player.getMoney() - playerCart.getTotalCost())
                        print("Purchase made. Money remaining:",Player.getMoney())
                        print("Shopping complete.\n")
                        Player.setAmmo(Player.getAmmo() + playerCart.getAmmoInCart())
                        Player.setFood(Player.getFood() + playerCart.getFoodInCart())
                        print("Ammo:",Player.getAmmo())
                        print("Food:",Player.getFood())
                        print("Wagons:",playerCart.getWagonInCart())
                        flag = False

                elif purchaseConfirmed == False:
                    print("Purchase not confirmed. Returning to menu...")
                    time.sleep(1)
                
                    
            else:
                    print("Invalid input.\nYou appear to have entered a number that was not on the menu.")
                    
        except ValueError:
                print("\n\nInvalid.\ntry to put in a real number please.\n\n")
                
        except TypeError:
                print("\n\nInvalid.\n\n")
                

