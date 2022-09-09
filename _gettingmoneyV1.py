#09/09/2022
#the purpose of this program is to print a virtual cheque for a users overtime pay etc - this is the rough draft V1. It will be updated over time.
import turtle #import libraries needed for cheque graphic

print("hello user! This program prints a virtual paycheck for you. pretty great right?") #intro - explain to user programs purpose
x = str(input("To start off with, what is the name of the employee you are printing the paycheck for?")) #employee name (x)
y = int(input("Great! What is the employees hourly rate? $")) #employees hourly rate (y)
z = int(input("Thanks! What is the employees number of hours worked? $")) #number of hours worked (z)

if (z > 40): #calculate hours and any overtime pay with if else statement
    b = z - 40 #number of overtime hours worked 
    s = y*1.5 #pay rate for overtime hours 
    m = s*b #pay for amount of overtime hours worked
    q = 40*y #pay for normal amount of hours worked
    d = (m+q) #total pay earned
    #please note: I used the textbook to assist in this part - cited below
    #Wentworth, P., Downey, A. B., Elkner, J., &amp; Meyers, C. (2020, April 17). How to Think Like a Computer Scientist: Learning with Python 3 Documentation.
    #Retrieved September 9, 2022,from https://buildmedia.readthedocs.org/media/pdf/howtothink/latest/howtothink.pdf 
    turtle.write(" Bank of Aldovi, 800 Uptown St, Jillyville AL, LGH 76J") #bank adress using turtle 
    turtle.forward(500) #underline bank adress/draw first line of rectangle for cheque
    turtle.left(90) #turn the turtle left 90 degrees
    turtle.forward(250) #turtle moves up to draw the second line of rectangle for cheque
    turtle.left(90) #turtle turnes left 90 degrees
    turtle.forward(500) #turtle moves to the left to draw the third line of the rectangle / cheque
    turtle.left(90) #turtle turns left 90 degrees
    turtle.forward(250) #turtle moves down to complete the rectangle cheque shape
    turtle.left(90) #turtle turns left 90 degrees
    turtle.right(90) #turtle turns right 90 degrees
    turtle.backward(200) #turtle moves up by 200 to top of cheque to begin writing
    turtle.write(" Employee Paycheck             Check Number: 85913") #turtle writes paycheck title and number
    turtle.forward(30) #turtle moves forward by 30 to space out the lines
    turtle.write(" Name of Employee:" + x + " Date:09/09/22") #writes name of employee by inserting input for variable x and includes the date
    turtle.forward(30) #turtle moves forward 30 to space out the lines
    turtle.write(" Address: 231 Blue Drive") #employee address
    turtle.forward(20) #turtle moves down 20 to space ut lines
    turtle.write("              Jillyville, AL HM1 P9K") #employee address continued 
    turtle.forward(62)
    turtle.write(" Amount($):           Please Sign Here:____________") #signiture area and amount 
    turtle.forward(20) #turtle moves down to space out lines
    turtle.write(d) #print variable d (total pay)
    
else:
    q = z*y #calculate the total pay earned (q)
    #this is the same stuff as above and has the same purpose so because of that I wont annotate it twice.
    #it is essentailly the making of the cheque
    turtle.write(" Bank of Aldovi, 800 Uptown St, Jillyville AL, LGH 76J")
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.right(90)
    turtle.backward(200)
    turtle.write(" Employee Paycheck             Check Number: 85913")
    turtle.forward(30)
    turtle.write(" Name of Employee:" + x + " Date:09/09/2022")
    turtle.forward(30)
    turtle.write(" Address: 231 Blue Drive")
    turtle.forward(20)
    turtle.write("              Jillyville, AL HM1 P9K")
    turtle.forward(62)
    turtle.write(" Amount($):           Please Sign Here:____________")
    turtle.forward(20)
    turtle.write(q) #print variable q (total pay)
