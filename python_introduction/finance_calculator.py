#prompt for user's financial details

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))


#calculate monthly savings

monthly_savings = monthly_income - monthly_expenses


#calculate projected annual savings

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))


#displaying results

print("Your monthly savings are " + "$" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: " + "$" + str(projected_savings) + ".")