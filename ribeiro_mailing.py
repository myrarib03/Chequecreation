#myra ribeiro
#2022/09/27
#the purpose of this program is to prompt a user for a mass and then give the cost of mailing a letter with that mass

mass = int(input("Hello! what is the mass of the letter youd like to mail (g)? ")) #user inputs mass of letter

if mass <= 30: #if mass is less than equal to 30
    print("the cost of mailing your letter is 40 sinas") #print outcome to user
elif mass >= 30 and mass <= 50 : #if mass is greater than equal to thirty and less than equal to 50
    print("the cost of mailing your letter is 55 sinas") #print outcome to user
elif mass >= 50 and mass <=100 : #if mass is greater than equal to 50 and less than equal to 100
    print("the cost of mailing your letter is 100 sinas") #print outcome to user
else: #calculate cost of mailing letter above 100g
    y = mass - 100
    z = y / 50
    x = z*25
    w = 100 + x
    print("Your cost for mailing your letter is", w, "sinas") #print outcome

