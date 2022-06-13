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
            monthly.append(monthly[i - 1]*(1 + float(i_r) /100))
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
            monthly.append(monthly[i-1]*(1 - i_r /100))
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
        
peytoncal() 