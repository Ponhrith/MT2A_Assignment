#asking users to between 2 modes
def options():
    print("Whose calculation do you want to see?")
    print("1.Josh.") #this mode will print the table that shows the projection of the month that users selected and the previous month
    print("2.Peyton.")#this mode only print the table that show the projection of the month that users selected
def option():
    print("Do you want to start again?")#when the each mode end we will ask the users if they want to start again
    print("1. Yes")
    print("2. No")
def initial():
    loop = True
    while loop:
        options()
        choices = input("Please select Option 1 or 2:")
        if choices =='1':
            josh()
#test
            while loop:
                option()
                choice = input("Please select Option 1 or 2:")
                if choice == '1':
                    initial()
                elif choice == '2':
                    print("Thank you for using our service!")
                    loop = False
                    break
                else:
                    print("Invalid Option. Please select Option 1 or 2.")#if users did not choose 1 or 2 then the option is invalid
        elif choices =='2':
            peyton()
            while loop:
                 option()
                 choice = input("Please select Option 1 or 2:")
                 if choice == '1':
                     initial()
                 elif choice == '2':
                     print("Thank you for using our service!")
                     loop = False
                     break
                 else:
                     print("Invalid Option. Please select Option 1 or 2.")
        else:
             print("Invalid Option. Please select Option 1 or 2.")
def josh():
    amount = int(input("Enter the amount of one time deposit:"))
    i_r = int(input("Enter the amount of annual interest rate:"))
    duration = int(input("Enter the duration of the deposits in years:"))
    monthly = []
    # print('total =  ', amount * ( (1 + i_r / 100) ** duration ))
    for i in range(duration):
        if i > 0:
            monthly.append(monthly[i - 1] *(1 + i_r / 100) )  # i=1,2,3,4...n
        else:
            monthly.append(amount * (1 + i_r / 100) ** (i + 1))  # i =0
        print("The Total Value to Date is:", round(monthly[i], 2))
    table = []
    print("THE PROJECTION OF INTEREST MADE BY AN INVESTMENT OF " + str(amount) +
          " EVERY YEAR AT AN INTEREST RATE OF " + str(i_r) + "% FOR A PERIOD OF " + str(duration) + " YEARS")
    for i in range(duration):
        #if i > 0:
        table.append([i + 1,  round(monthly[i])] )
        #else:
        #    table.append([i + 1,   round(monthly[i] - amount, 2),round(monthly[i] - amount * (i + 1), 2), round(monthly[i], 2)])
    for v in table:
        a, b= v
        print("{:<8} {:<10}".format(a, b))
def peyton():
    print("IN THIS INVESTMENT WE EXPECT TO HAVE EXACT 21 YEARS OF GOOD RETURN AND 9 YEARS OF BAD RETURN")
def earn():
    print("PRESS 1 TO SEE THE GOOD RETURN:")  #peyton calculation is divided into two parts so i gave the users options
    print("PRESS 2 TO SEE THE BAD RETURN:")   #giving them options not to make the program messy

def peytoncal(): #define the main function asking them to choose
    loop = True
    while loop:
        earn()
        see = input("Please select Option 1 or 2:")  
        if see == '1':
            good()
        elif see == '2':
            bad()
        else: 
            print("Invalid Option. Please select Option 1 or 2.")

def good(): #define good function for the good return for the 21 years
    amount = int(250000) # I assigned them value, so to let it run autmoatically when the user select any option
    i_r = float(17.5)
    duration = int(21)
    monthly = []
    for i in range(duration):
        if i > 0:
            monthly.append(monthly[i-1]*(1 + i_r /100))
        else:
            monthly.append(amount * (1 + i_r /100) ** (i + 1))
        print("The Total Value to Date is:", round(monthly[i], 2))
    table = []
    print("SUPPOSED THE FIRST 21 YEARS IS THE GOOD RETURN OF " + str(amount) +
          "EVER YEAR AT AN INTERST RATE OF" + str(i_r) + "%")
    for i in range(duration):
        table.append([i + 1, round(monthly[i])])
    for v in table:
        a, b = v
        print("{:<8} {:10}".format(a, b))
        
def bad(): #define bad return as the loss return for the 9 years
    amount = int(250000)
    i_r = float(7.5)
    duration = int(9)
    monthly = []
    for i in range(duration):
        if i > 0:
            monthly(monthly[i-1]*(1 - i_r /100))
        else:
            monthly.append(amount * (1 - i_r /100) ** (i + 1))
        print("The Total Value to Date is:", round(monthly[i], 2))
        
    table = []
    print("SUPPOSED THE FIRST 9 YEARS IS THE BAD RETURN OF " + str(amount) +
          "EVER YEAR AT AN INTERST RATE OF" + str(i_r) + "%")
    for i in range(duration):
        table.append([i + 1, round(monthly[i])])
    for v in table:
        a, b = v
        print("{:<8} {:10}".format(a, b)) 
        
 
initial()