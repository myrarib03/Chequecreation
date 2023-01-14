class address: #initalize class address
    
    def __init__(self,houseNum,street,postalCode, city, state, apartmentNum=None): #these are the neccissary variables to take into consideration - init is the constructor
        self.houseNum = houseNum #house number
        self.street = street #street
        self.postalCode = postalCode # house postal code
        self.apartmentNum = apartmentNum #apartment number
        self.city = city # city
        self.state = state #state
    
    def __str__(self): #create method to print the address
        if self.apartmentNum:
            return f"{self.houseNum} {self.street}, Apt. {self.apartmentNum}\n{self.city}, {self.postalCode}, {self.state}" #this is if there is an apartment number specified
        else:
            return f"{self.houseNum} {self.street}\n{self.city}, {self.postalCode}, {self.state}" #this is if there is not
    
    def comesBefore(self, other): #this determines which address comes first
        return self.postalCode < other.postalCode #postal codes are organized alphabetically and numerically
