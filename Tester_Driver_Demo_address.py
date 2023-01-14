from Ribeiro_address import address #import address class

Address1 = address(123, 'Main St', 'A13345', 'New York', apartmentNum='A', state = 'Washington') #initalize address 1
Address2 = address(4565, 'sixth line', '23ZL98', 'Oakville', state = 'Ontario') #initalize address 2


if Address1.comesBefore(Address2): #print the address that comes first based off postal code
    print(f"{Address1}\n\ncomes before...\n\n{Address2}")
else:
    print(f"{Address2}\n\ncomes before...\n\n{Address1}")