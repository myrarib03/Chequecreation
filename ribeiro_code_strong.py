#myra ribeiro
#2022/10/26
#purpose: to determine weater or not a password is good

password = input("Hello! Welcome to my program! This programs purpose is to determine if your passcode is good or not. Please enter your passcode here: ") #input and welcome statement

def strong_passcode(password): #define function 
    while len(password)>=8: #insert while loop while the length of the password is greater than equal to 8 - this determines the amount of characters in the string
            if password.isalpha() == True: #insert ifelse statement, password.isalpha() determines if the passcode has no numbers in it
                return("False missing number") #return false, passcode is missing a number
                break #break loop
            else: #if the passcode does have numbers in it
                if password.islower() == True: #if the passcode is entirely lowercase 
                    return("False no upper") #return false, passcode is missing an uppercase
                    break #break loop
                else: #if the passcode does have uppercase letters
                    if password.isupper() == True: #if the passcode contains no lowercase
                        return("False no lower") #return false, passcode is missing a lowercase
                        break #break loop
                    else: #if the passcode has a lowercase, check if there is any numbers at all
                        return(any(c.isalpha() for c in password))#check to see if any of the char in password are letters, any is true if any iterms in string are true
                        break
    if len(password) < 8: #if passcode char is less than 8
        return("False") #return false to user
            
print(strong_passcode(password)) #return the function

print("thank you for using my program! goodbye!") #goodbye statement