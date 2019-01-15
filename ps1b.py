# Problem Set 1: Problem #2 [SAVING, WITH A RAISE]
# Date Started: January 15, 2019
# Date Completed: January --, 2019

# Variables
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04  
num_of_months = 0

# User Input
annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

# Calculation from input
amount_needed = total_cost * portion_down_payment

# Loop to calculate savings each month
while(current_savings < amount_needed):
    monthly_salary = annual_salary/12
    num_of_months += 1
    current_savings += portion_saved*(monthly_salary) + ((r*current_savings)/12)
    if num_of_months%6 == 0:
        annual_salary += annual_salary*semi_annual_raise

# After savings become enough for down payment, number of months is printed
print("Number of months: " + str(num_of_months))
