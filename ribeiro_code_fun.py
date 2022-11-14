#myra ribeiro
#2022/11/03
#the purpose of this program is to transform a list with range of numbers -100 to 100.
#It transforms to a list of all ones, a list of random integers, a list of random positive integers,
#returns the sum of the positive integers, and then returns the indexes of all odd numbers out of the positive random integers.

import random #import random library

print("hello, welcome to my program! the purpose of this program is to transform a list with range of numbers -100 to 100. It transforms to a list of all ones, a list of random integers, a list of random positive integers, returns the sum of the positive integers and then returns the indexes of all odd numbers out of the positive random integers.") #hello statement
rand_list_1= [*range(0, 101)] #make list of range 0, 100 (write 101 cause the numbers and the number of elements arent the same)

rand_list_2 = [*range(-100, 0)] #make list of range  - 100, 0

rand_list = list(rand_list_2 + rand_list_1) #make list of range - 100 to 100 (this is the original list to be transformed)

print(rand_list)#print the list

result = list([element*0 for element in rand_list]) #multiply each element in the list to zero, makes every element 0

list_of_ones = list([element + 1 for element in result]) #add one to each element in the list, makes every element 1
print(list_of_ones)#print the list_of_ones
  
list_of_rands = list([element + random.randint(-100,100) for element in (list_of_ones)]) #add random numbers plus the existing values to all of the elements in the list to make it filled with random numbers
print(list_of_rands) #print the list of random numbers

list_of_positive_rands = list([abs(element) for element in (list_of_rands)]) #use the absolute value function on each element in the list in a for loop to make them all positive
print(list_of_positive_rands) #print the list of positive random numbers

sampleSum = sum(list_of_positive_rands) #print the sum of the positive random numbers
print(sampleSum) #return value to user

for (index,element) in enumerate(list_of_positive_rands): #use a for loop with enumerate function to determine the index for every value in list_of_positive_rands
    if element % 2 != 0: #if the remander of the value divided by 2 is not equal to zero it is odd
        print("list[", index, "],", end = '') #reuturn the indexes of the odd numbers in the list to user


print(" thanks for using my program! goodbye!") #goodbye statement