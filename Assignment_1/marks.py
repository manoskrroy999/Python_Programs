'''If the marks obtained by a student in five different subjects are input through the keyboard,
find out the aggregate marks and percentage marks obtained by the student. Assume that the
maximum marks that can be obtained by a student in each subject is 100.'''



m1=int(input("Enter marks in subject 1: "))
m2=int(input("Enter marks in subject 2: "))
m3=int(input("Enter marks in subject 3: "))
m4=int(input("Enter marks in subject 4: "))
m5=int(input("Enter marks in subject 5:"))

sum=m1+m2+m3+m4+m5
avg=sum/5
print("Aggregate marks is: ",sum)
print("Percentage marks obtained by the student is: ",avg,"%")