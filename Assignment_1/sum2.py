'''If a five-digit number is input through the keyboard, write a program to calculate the sum of
its digits.(Hint: Use the modulus operator ‘%’)'''


num=(int(input("Enter a number: ")))
sum=0
while(num>0):
    a=num%10
    sum=sum+a
    num=num//10
print("Sum of digits is: ",sum)