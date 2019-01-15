# Problem Set 1: Problem #1 [HOUSE HUNTING]
# Date Started: January 14, 2019
# Date Completed: January 14, 2019

# Variables
portion_down_payment = 0.25
current_savings = 0.0
r = 0.04  
num_of_months = 0

# User Input
annual_salary = float(input("Enter your starting annual salary: "))
monthly_salary = annual_salary/12
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

# Calculation from input
amount_needed = total_cost * portion_down_payment

# Loop to calculate savings each month
while(current_savings < amount_needed):
    num_of_months += 1
    current_savings += portion_saved*monthly_salary + ((r*current_savings)/12)

# After savings become enough for down payment, number of months is printed
print("Number of months: " + str(num_of_months))
