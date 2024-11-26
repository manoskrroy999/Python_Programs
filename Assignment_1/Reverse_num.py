'''If a five-digit number is input through the keyboard, write a program to reverse the number.'''


number = input("Enter a five-digit number: ")

if len(number) == 5 and number.isdigit():
    reversed_number = number[::-1]
    print(f"Reversed number: {reversed_number}")
else:
    print("Invalid input. Please enter a five-digit number.")
