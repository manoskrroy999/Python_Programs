 # Input basic salary
basic_salary = float(input("Enter Ramesh's basic salary: "))

# Calculate dearness allowance and house rent allowance
dearness_allowance = 0.40 * basic_salary
house_rent_allowance = 0.20 * basic_salary

# Calculate gross salary
gross_salary = basic_salary + dearness_allowance + house_rent_allowance

# Display the result
print(f"Ramesh's Gross Salary is: {gross_salary}")
