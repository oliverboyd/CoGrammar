import math
print('''investment - to calculate the amount of interest you'll earn on your investment
      bond - to calculate the amount you'll have to pay on a home loan
      
      Enter either 'investment' or 'bond' from the menu above to proceed:''')
type = input()
if type.lower() == "investment" :
    print("Please input the amount of money you are depositing.")
    deposit = float(input())
    print("Please input the interest rate. (as a percentage)")
    interest_rate = float(input())
    print("Please input the number of years for which you plan to invest.")
    time = int(input())
    print("Simple or compound interest?")
    interest_type = input()
    if interest_type.lower() == "simple":
        A = deposit*(1 + (interest_rate/100)*time)
        print("Total amount: " + str(A))
    elif interest_type.lower() == "compound":
        A = deposit*math.pow((1+(interest_rate/100)),time)
        print("Total amount: " + str(A))
    else: print("Invalid input.")
elif type.lower() == "bond":
    print("Please input the value of the house.")
    value = float(input())
    print("Please input the interest rate. (as a percentage)")
    interest_rate = float(input())
    print("Please input the number of months you plan to take to repay the bond.")
    time = int(input())
    repayment = (((interest_rate/100)/12) * value) / (1 - (1 + ((interest_rate/100)/12)) ** (-time))
    print("You will have to pay back " + str(repayment) + " each month." )
else: print("Invalid input.")