'''The length & breadth of a rectangle and radius of a circle are input through the keyboard.
Write a program to calculate the area & perimeter of the rectangle, and the area &
circumference of the circle.'''


l=int(input("Enter Length of Rectangle: "))
b=int(input("Enter Breadth of Rectangle: "))
a=l*b
p=2*(l+b)
print("Area of Rectangle: ",a)
print("Perimeter of Rectangle: ",p)
r=(int(input('Enter the radius of the circle:')))
c=2*3.14*r
cr= 3.14*(r**2)
print("Area of Circle: ",cr)
print("Circumference of Circle: ",c)