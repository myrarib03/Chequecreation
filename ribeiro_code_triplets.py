#myra ribeiro
#2022/10/22
#purpose: to compute and return all pythagorean triples back to user up to their inputted integer

#citation: Parody, L. (2017, October 6). Calculating pythagorean triplets in elixir, python and JavaScript. Medium. Retrieved October 22, 2022, from https://medium.com/@lizparody/pythagorean-triplets-in-elixir-python-and-javascript-638f6a60494#:~:text=%E2%80%94%20Pythagorean%20Triples%20consists%20of%20three,16%20%3D%2025%20a%20Pythagorean%20Triple! 

import math #import math library 

limit = int(input("hello! the purpose of this program is to return all pythag triples based off your givien integer. please enter your number here:")) #welcome statement and user enters integer limit for program

def pythag_triplet(n): #call and define the function, function can take one argument n, n is equal to to the users inputted limit 
  for a in range(n): #define the list in which 'a' can be used for pythag triple. a must be less than c. 
    for b in range(1, a): #define the list in which 'b' can be used for pythag triple. b must be less than a and less than c.
        c = math.sqrt(a**2 + b**2) #calculate c by using the pythag triple formula and using the math library to square root it.
        if c % 1 == 0: #ensure c is not a decimal by using modulo. if remainder is above zero,c is a decimal.
            if c <= limit: #if c is less than or equal to the users inputted limit
                print(a, b, int(c)) #program returns the pythagorean triples up to the inputted limit. 
            
pythag_triplet(limit) #pythagorean triplet function with limit

print("thanks for using my program, goodbye!") #goodbye statement