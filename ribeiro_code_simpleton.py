#myra ribeiro
#2022/10/05
#the purpose of this program is to compute the payable tax or refund due for simpleton citizens (an imaginary city)

income = float(input("Hello! This program calculates payable tax or refund due for simpleton citizens. to begin, what is your income ($)? ")) #input user income
houseCost = float(input("what is your housing cost ($)? ")) #inputn user house cost
totalChildren = float(input("what is the number of children in your house? ")) #input total children in the household
schoolChildren = float(input("what are the kids in school that you have? ")) #input number of school children in the household
tax_rate = 0.18 #simpleton tax rate

tax_additions = income*tax_rate #calculate the taxes without deductions or additions

if houseCost > 8000: #calculate the tax rate if the house cost is over 8000
    new_tax = tax_additions - 10000 #calculate the tax for simpleton citizens if they make more than 10000
    if new_tax > 2000: #calculate the interest rate if the tax us more than 2000
        tot_tax = new_tax*0.15 #interest
        new_total_tax = new_tax + tot_tax #add interest to tax rate
        print("$", new_total_tax, "is your tax payable") #print tax payable to user
    elif new_tax < 2000 and new_tax > 0: #if the taxes are less than 2000 but greater than zero
        print("$", new_tax, "is your tax payable.") #print tax payable to user
    elif new_tax < 0: #calculate if the taxes are less than zero
        print("$", new_tax - new_tax - new_tax, "is your tax refundable") #convert to a positive number and return tax refundable to user

elif houseCost < 6000 and totalChildren > 2 and schoolChildren >= 1: #calculate if the house cost is less than 6000 and the total children in the househodl is greater than 2 and there is one or more kids in school
    non_school_children = totalChildren - schoolChildren #calculate number of children not in school
    childTax = non_school_children*500 #tax for kids not in school
    schoolChildTax = schoolChildren*1000 #tax for kids in school
    total_tax = tax_additions - childTax - schoolChildTax #the total tax after including school and not school children
    if total_tax < 0: #if the total tax is less than zero it becomes a refundable
        new_total_tax = total_tax - total_tax - total_tax #make number positive
        print("$", new_total_tax, "is your tax refundable") #return value to user
    elif total_tax > 2000: #if the total tax is over 2000 then it is taxed 15%
        n_total_tax = total_tax*0.15 #calculate the interest
        print("$", n_total_tax + total_tax, "is your tax payable") #add interest to non interest and return value to user 
    else:
        print("$", total_tax, "is your tax payable") #return value to user
else:
    if tax_additions > 2000: #if the tax is more than 2000
        tax_surplus = tax_additions*0.15 #calculate interest
        new_payable = tax_additions + tax_surplus #add interest to tax
        print("$", new_payable, "is your tax payable") #return value to user
    elif tax_additions < 2000: #if tax is less than 2000
        print("$", tax_additions, "is your tax payable") #return value to user
    
print("thanks for using my program! goodbye!") #goodbye statement
