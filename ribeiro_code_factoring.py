#myra ribeiro
#2022/10/20
#the purpose of this program is to determine and return all of the factors of the inputted user number

integer = int(input("Hello, welcome to my program! please enter your number: "))
#hello statment and input

i = 1 #set i to 1

while i <= integer: #use while loop to determine and print the factors 
    factors = integer % i #Assign variables and calculate 
    if factors == 0: #if factors are equal to 0
        print (f"{i} is a factor") #print the factors of integer
    i = i + 1 #determines integers you are dividing by up to 'integer'

print("thanks for using my program! goodbye!") #goodbye statement