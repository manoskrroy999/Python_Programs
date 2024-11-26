'''Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of basic
salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross
salary.'''


 # Input basic salary
basic_salary = float(input("Enter Ramesh's basic salary: "))

# Calculate dearness allowance and house rent allowance
dearness_allowance = 0.40 * basic_salary
house_rent_allowance = 0.20 * basic_salary

# Calculate gross salary
gross_salary = basic_salary + dearness_allowance + house_rent_allowance

# Display the result
print(f"Ramesh's Gross Salary is: {gross_salary}")
