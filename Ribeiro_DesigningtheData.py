class CashRegister :
   ## Constructs a cash register with cleared item count and total.
   #  @param taxRate the tax rate to use with this cash register
   #
   def __init__(self, taxRate) :
      self._itemCount = 0 #initalize variable itemcount and set to zero
      self._totalPrice = 0.0 #set total price to zero
      self._taxableTotal = 0.0 #set the taxable total to zero
      self._taxRate = taxRate 
      self._previous_prices = [] #set list of previous prices to zero
      
   ## Adds an item to this cash register.
   #  @param price the price of this item
   #  @param taxable True if this item is taxable
   #
   def addItem(self, price, taxable) : #adds item to cash register
      self._itemCount = self._itemCount + 1 #adds item to the item count
      self._totalPrice = self._totalPrice + price #calculates the untaxed price
      if taxable :
         self._taxableTotal = self._taxableTotal + price
      self._previous_prices.append((price, taxable)) #assign all of the prices to the list previous prices
      
   ## Removes the most recent item from this cash register.
   #
   def undo(self):#adds undo to the class
      if self._itemCount > 0: #if the item count is greater than zero
         self._itemCount = self._itemCount - 1 #take away the previous item from the itemcount
         price, taxable = self._previous_prices.pop() #take away the the price from the list previous prices
         self._totalPrice = self._totalPrice - price#take away the price all together
         if taxable:
            self._taxableTotal = self._taxableTotal - price #remove tax if taxable
      
   ## Gets the price of all items in the current sale.
   #  @return the total price
   #
   def getTotal(self) : #returns price of items in the current sale
      return self._totalPrice + self._taxableTotal * self._taxRate / 100 
      
   ## Gets the number of items in the current sale.
   #  @return the item count
   #
   def getCount(self) : #returns the total number of items in the current sale
      return self._itemCount

   ## Clears the item count and the total.
   #  
   def clear(self) :
      self._itemCount = 0
      self._totalPrice = 0.0
      self._taxableTotal = 0
      self._previous_prices = []
      



#test for the class...
register1 = CashRegister(7.5)
register1.addItem(3.95, False)
register1.addItem(19.95, True)
register1.addItem(2300, False)
register1.undo()
print(register1.getCount())
print("Expected: 2")
print("%.2f" % register1.getTotal())
print("Expected: 25.40")
