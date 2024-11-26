'''Two numbers are input through the keyboard into two locations C and D. Write a program to
interchange the contents of C and D.'''


# Input two numbers
C = int(input("Enter the first number (C): "))
D = int(input("Enter the second number (D): "))

# Swapping the values
C, D = D, C

# Display the swapped values
print(f"After swapping: C = {C}, D = {D}")
