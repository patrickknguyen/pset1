# Part B: Saving, With a Raise

annual_salary = float(input("Input annual salary: "))
portion_saved = float(input("Input portion of salary saved for down payment, as a decimal: "))
total_cost = float(input("Input total cost of house: "))
semi_annual_raise = float(input("Input semi annual raise, as a decimal: "))

down_payment_rate = 0.25
annual_return = 0.04

portion_down_payment = total_cost * down_payment_rate
monthly_saved = (annual_salary / 12) * portion_saved
current_savings = 0.0
number_of_months = 0

while current_savings < portion_down_payment:
    current_savings += monthly_saved + (current_savings * annual_return /12)
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_saved = (annual_salary / 12) * portion_saved
    
    
    
print("Assuming the down payment is at " + str(down_payment_rate * 100) + "%, and your annual return on investment is at " + str(annual_return * 100) + "%, it will take you " + str(number_of_months) + " months of saving")
