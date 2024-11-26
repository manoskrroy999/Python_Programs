'''If a four-digit number is input through the keyboard, write a program to obtain the sum of the
first and last digit of this number.'''


number = int(input("Enter a five-digit number: "))
sum_of_digits = 0

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    number = number //10

print("The sum of the digits is:", sum_of_digits)
