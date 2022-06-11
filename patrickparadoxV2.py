#asking users to between 2 modes
def options():
    print("How would you like to see your projection?")
    print("1.The month I selected & the previous month.") #this mode will print the table that shows the projection of the month that users selected and the previous month
    print("2.Just the month I selected.")#this mode only print the table that show the projection of the month that users selected
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
            result1()
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
            result2()
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
def result1():
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
def result2():
    amount = int(input("Enter the amount of deposit:"))
    i_r = int(input("Enter the amount of interest rate:"))
    duration = int(input("Enter the duration of the deposits in months:"))
    monthly = []
    for i in range(duration):
        if i > 0:
            monthly.append(monthly[i - 1] + amount *(1 + i_r / 1200) ** (i + 1))  # i=1,2,3,4...n
        else:
            monthly.append(amount * (1 + i_r / 1200) ** (i + 1))  # i =0
        print("The Total Value to Date is:", round(monthly[i], 2))
    table = []
    print("THE PROJECTION OF INTEREST MADE BY AN INVESTMENT OF " + str(amount) +
          " EVERY MONTH AT AN INTEREST RATE OF " + str(i_r) + "% FOR A PERIOD OF " + str(duration) + " MONTHS")
    for i in range(duration):
        if i > 0:
            table.append([i + 1, amount, amount * (i + 1), round(monthly[i] - monthly[i - 1] -amount, 2),round(monthly[i] - amount * (i + 1), 2), round(monthly[i], 2)])
        else:
            table.append([i + 1, amount, amount * (i + 1), round(monthly[i] - amount, 2),round(monthly[i] - amount * (i + 1), 2), round(monthly[i], 2)])
        for v in table:
            a, b, c, d, e, f = table[duration - 1]
            print("{:<8} {:<10} {:<20} {:<25} {:<25} {:<8}".format(a, b, c, d, e, f))
initial()