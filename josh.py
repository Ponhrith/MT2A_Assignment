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
    table.append([i + 1,  round(monthly[i])] )
    
for v in table:
    a, b= v
    print("{:<8} {:<10}".format(a, b))