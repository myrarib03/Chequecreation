#myra ribeiro
#2022/10/11
#the purpose of this program is to calculate Pi using the lebiniz formula based on the users specified number of iterations
#citations:
#Calculate Pi with python. GeeksforGeeks. (2021, May 19). Retrieved October 11, 2022, from https://www.geeksforgeeks.org/calculate-pi-with-python/ 

iterations = int(input("Hello! this program will calculate pi based on your input of iterations. please enter the number of iterations:")) #user inputs number of iterations

k = 1 #denominator is 1, will be increased by 2

sum_ = 0 #sum is zero

for i in range (iterations): #for the item in the list iterations
    if i%2 == 0: #if the remainder of i divided by 2 is zero
        sum_ += 4/k #adds the value to the variable and assigns the result to that variable (even = positive)
    else: #if it is not zero
        sum_ -= 4/k #subtracts the value to the variable and assigns the result to that variable (odd = negative)
        
    k += 2 #the denominator is odd, increasing by 2
    
print("your value of pi is:", sum_, "thank you for using my program! goodbye!") #return value and goodbye statement