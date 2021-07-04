#This program is a financial calculator. The program requests key information from the user and provides the user with a projected simple/compound interest value.
#This program also calculates and displays to user monthly bond repayments

import math

#Request for user to enter investment or bond based on the calculation the user requires
selected_calculation = input('''Choose either \'investment\' or \'bond\' from the menu below to proceed:

investment  - to calculate the amount of interest you'll earn on interest
bond        - to calculate the amount you'll have to pay on a home loan
''')

#Convert user input to lowercase
selected_calculation_lowercase = selected_calculation.lower()

#Based on user input, the appropriate condition is selected. The program prompts the user to enter key information and the program displays the calculation to the user.
if(selected_calculation_lowercase == "investment"):
    initial_deposit = float(input("Please enter the amount of money you are depositing: R"))
    interest_rate = float(input("Please enter the interest rate %: "))
    no_of_years = float(input("Please enter the number of years you plan to invest for: "))
    interest = input("Please enter the type of interest: \'simple\' or \'compound\': ")

    if(interest == "simple"):
        total = round((initial_deposit * (1+(interest_rate/100)*no_of_years)),2)
        print(f"Based on the information provided, the future investment value: R{total}")
    else:
        total = round(initial_deposit * math.pow((1+(interest_rate/100)),no_of_years),2)
        print(f"Based on the information provided, the future investment value: R{total}")
        
elif(selected_calculation_lowercase == "bond"):
    present_value_of_house = float(input("Please enter the present value of the house: R"))
    interest_rate = float(input("Please enter the interest rate %: "))
    no_of_months = float(input("Please enter the number of months you plan to take to repay the bond: "))
    monthly_repayment = round((((interest_rate/100)/12)*present_value_of_house) / (1-(math.pow((1+((interest_rate/100)/12)),(no_of_months * -1)))),2)
    print(f"Your monthly repayment will be R{monthly_repayment}")
    
#If the user does not enter "investment" or "bond", an error message is then displayed
else:
    print("ERROR! YOU HAVE NOT SELECTED A VALID OPTION. \nPlease input \'investment\' or \'bond\' only")
