class CashRegister :
   ## Constructs a cash register with cleared item count and total.
   #  @param taxRate the tax rate to use with this cash register
   
   def getChange(self, payment): #get change method
        change = payment - self.getTotal() #this is the change
        self.clear() #clears the register
        return change #change is returned
    
   def __init__(self, taxRate) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._taxableTotal = 0.0
      self._taxRate = taxRate
      
   ## Adds an item to this cash register.
   #  @param price the price of this item
   #  @param taxable True if this item is taxable
   #
   def addItem(self, price, taxable) :
      self._itemCount = self._itemCount + 1
      self._totalPrice = self._totalPrice + price
      if taxable :
         self._taxableTotal = self._taxableTotal + price
      
   ## Gets the price of all items in the current sale.
   #  @return the total price
   #
   def getTotal(self) :
      return self._totalPrice + self._taxableTotal * self._taxRate / 100
      
   ## Gets the number of items in the current sale.
   #  @return the item count
   #
   def getCount(self) :
      return self._itemCount

   ## Clears the item count and the total.
   #  
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._taxableTotal = 0
   
   def getDollars(self) : #implement getDollars
      return int(self.getTotal()) #rounds the total to an integer value and prints without the cents


#test below...
register1 = CashRegister(7.5)
register1.addItem(3.95, False)
register1.addItem(19.95, True)
print("%.2f" % register1.getChange(30.00))
print("Expected: 4.05")