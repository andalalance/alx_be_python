#Use user input, variables, and arithmetic operations to
# calculate and provide feedback on a user’s monthly savings 
# and potential future savings without applying conditional statements.

monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your total monthly expenses: "))

monthlySaving = monthlyIncome - monthlyExpenses

print(f"Your monthly savings are ${monthlySaving}")
print(f"Projected savings after one year, with interest, is: ${monthlySaving * 12 + (monthlySaving * 12 * 0.05)}.")

