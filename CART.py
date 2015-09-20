class Cart:
    def __init__(self):
        self.foodInCart = int(0)
        self.ammoInCart = int(0)
        self.wagonInCart = int(0)
        self.priceFood = float(.20)
        self.priceAmmo = float(.10)
        self.priceWagon = int(300)
        self.totalCost = int(0)

    #accessors
    def getFoodInCart(self): return self.foodInCart
    def getAmmoInCart(self): return self.ammoInCart
    def getWagonInCart(self): return self.wagonInCart
    def getPriceFood(self): return self.priceFood
    def getPriceAmmo(self): return self.priceAmmo
    def getPriceWagon(self): return self.priceWagon
    def getCostFood(self): return int(self.priceFood * self.foodInCart)
    def getCostAmmo(self): return int(self.priceAmmo * self.ammoInCart)
    def getCostWagon(self): return int(self.priceWagon * self.wagonInCart)
    def getTotalCost(self): return int(self.getCostFood() + self.getCostAmmo() + self.getCostWagon())
    
    


    #mutators
    def setFoodInCart(self, newFoodInCart): self.foodInCart = newFoodInCart
    def setAmmoInCart(self, newAmmoInCart): self.ammoInCart = newAmmoInCart
    def setWagonInCart(self, newWagonInCart): self.wagonInCart = newWagonInCart
    def setPriceFood(self, newPriceFood): self.priceFood = newPriceFood
    def setPriceAmmo(self, newPriceAmmo): self.priceAmmo = newPriceAmmo
    def setPriceWagon(self, newPriceWagon): self.priceWagon = newPriceWagon
    def setCostFood(self, newCostFood): self.costFood = newCostFood
    def setCostAmmo(self, newCostAmmo): self.costAmmo = newCostAmmo
    def setCostWagon(self, newCostWagon): self.costWagon = newCostWagon
    def setTotalCost(self, newTotalCost): self.totalCost = newTotalCost
    
    #other functions
    
         
    def displayCart(self):
        print("\nYour cart currently contains:")
        if self.getFoodInCart() > 0:
            print("Food(in pounds): ", self.getFoodInCart())
        if self.getAmmoInCart() > 0:
            print("Ammo(in bullets):", self.getAmmoInCart())
        if self.getWagonInCart() == 1:
            print("Wagon: One wagon ready to go.")
    def clearCart(self):
        self.setFoodInCart(0)
        self.setAmmoInCart(0)
        self.setWagonInCart(0)
