#myra ribeiro
#2022/11/19
#the purpose of this program is to read 1000 floating point data values and print out the count of the values, the average, and the standard deviation.

import random #import random library
import ribeiro_code_fun #import 1000 random number file

print("hello! welcome to my program. the purpose of this program is to read 1000 floating point data values and print out the count of the values, the average, and the standard deviation.") #hello statement
rand_list = [*range(1,1001)] #define random list

sumxi = sum(ribeiro_code_fun.random_list(rand_list)) #sum all of the random values

print("the count of the values is", sumxi) #return the sum to user

xb = sumxi/1000 #divide sum by 1000 (because there is 1000 values in the list (n = 1000))

print("the average of the values is", xb) #return the average of the values 

new_list = list([(xi - xb)**2 for xi in (ribeiro_code_fun.random_list(rand_list))]) #create a new list with every individual value in the list subtracted by the average and squared

e = (sum(new_list)/999) #the sum of all of the values in new_list. The sum is divided by 999 (n-1)

s = e**(1/2) #square root e, that way you can get 's' or the standard deviation

print("the standard deviation is", s) #return the standard deviation to user

print("goodbye! thanks for using my program.") #goodbye statement