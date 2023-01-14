class CashRegister: #define class cash register
    def __init__(self, taxRate): #constructor 
        self._itemCount = 0 #set item count to zero
        self._totalPrice = 0.0 #set total price to zero
        self._taxableTotal = 0.0 #set taxable total to zero
        self._taxRate = taxRate #set tax rate
        self._salesTotal = 0 #set sales total to zero
        self._salesCount = 0 #set sales count to zero
    
    def addItem(self, price, taxable): #method additem - adds an item to the cash register
        self._itemCount = self._itemCount + 1 #set the item count variable to the amount of items added
        self._totalPrice = self._totalPrice + price #set the total price to the amount of items added
        if taxable: #calculate the tax on the item
            self._taxableTotal = self._taxableTotal + price #calculate tax
        self._salesTotal += self._totalPrice + self._taxableTotal * self._taxRate / 100 #set the total sales for the item
        self._salesCount += 1 #set the total sales count
    
    def getTotal(self): #set the total of the sales made in that transaction
        return self._totalPrice + self._taxableTotal * self._taxRate / 100
    
    def getCount(self): #set the total of the items in that transaction
        return self._itemCount
    
    def clear(self): #clear that specific transaction
        self._itemCount = 0
        self._totalPrice = 0.0
        self._taxableTotal = 0
    
    def getSalesTotal(self): #get the total price of sales made throughout the day with the cash register
        return self._salesTotal
    
    def getSalesCount(self): #get the count of the sales made throught the day with the cash register
        return self._salesCount
    
    def resetSales(self): #set all count and total sales to zero for a new day
        self._salesTotal = 0
        self._salesCount = 0


#test below...
register = CashRegister(7.5) #set tax
register.addItem(3.95, False) #first item
register.addItem(19.95, True) #second item
sales_total = register.getSalesTotal() #total price of all daily sales before cleared
sales_count = register.getSalesCount() #total count of all sales before cleared
print(sales_total) #print to user
print(sales_count)
register.resetSales() #reset all sales
new_sales_total = register.getSalesTotal() #total after cleared
new_sales_count = register.getSalesCount()
print(new_sales_total) #print to user
print(new_sales_count)