#myra ribeiro
#2022/11/19
#the purpose of this module is to generate 1000 random numbers from 1-1000

import random #import random library

rand_list = [*range(1,1001)] #define random list

def random_list(rand_list):#create function rand_list
    result = list([element*0 for element in rand_list]) #make the elements in rand_list == 0
    list_of_rands = list([element + random.randint(1,1001) for element in (result)])#add element plus the random numbers from 1 - 1001
    return(list_of_rands)#return the list of random numbers

print(random_list(rand_list))#print to make sure you have the correct function