#myra ribeiro
#2022/09/23
#this programs purpose is to display the dimensions of a letter size sheet of papet in millimetres, nanometres and picometres.
#citations: (chicago style)
#Samath. “ Java Program That Displays the Dimensions of a Letter­Size (8.5 × 11 Inch) Sheet of Paper in Millimeters.”
#Java program that displays the dimensions of a lettersize (8.5 × 11 inch) sheet of paper in millimeters, February 8, 2021.
#https://sourcecodeera.com/blogs/Samath/Java-program-that-displays-the-dimensions-of-a-letter%C2%ADsize-(85-%C3%97-11-inch)-sheet-of-paper-in-millimeters.aspx.
#“Convert Inch to Nanometer.” UnitConverters.Net. Accessed September 23, 2022. https://www.unitconverters.net/length/inch-to-nanometer.htm.
#Python round() function. Accessed September 23, 2022. https://www.w3schools.com/python/ref_func_round.asp. 



#user greeting and purpose 
print("Hello! Welcome to my program. This program prints the dimensions of a letter size sheet of paper (8.5 inch x 11 inch) in milimetres, nanometres, and picometres.")
#assign variables and calculate dimensions in mm
x = round(8.5*25.4) #round function ensures its not a crazy decimal you are getting back
y = round(11*25.4)# the * is for multiplication
#print answer in mm
print(x,"mm x", y, "mm")
print("that is your dimensions in milimetres")
#caclulate answer in nm and assign variables
w = round(8.5*25400000)
z = round(11*25400000)
#print answer in nm for user to see
print(w,"nm x", z, "nm")
print("that is your dimensions in nanometres")
#calculate answer in pm and assign variables
m = round(w*1000)
n = round(z*1000)
#print answer in pm for user to see
print(m,"pm x", n, "pm")
print("that is your dimensions in picometres")