a = 5
b = -10

print("a<<b =",a<<1) # This is left
print("a>>b=" , a>>1) # This is right

a = 10
b = -5

print("a<<b =",a<<1) # This is left
print("a>>b = ",a>>1) # This is right

maths = int(input("Enter the marks of students in maths"))
english = int(input("Enter the marks of students in english"))
hindi = int(input("Enter the marks of students in hindi"))
science = int(input("Enter the marks of students in science"))
sst = int(input("Enter the marks of social science"))

total = maths+english+hindi+science+sst
average = total/5

print("The total of the student is ",total)
print("The average marks of the students is",average)

if average >= 91 and average <= 100:
    print("Your grade is a1")
elif average >= 81 and average <= 91:
    print("Your grade is a2")
elif average >= 71 and average <= 81:
     print("Your grade is b1")
elif average >= 61 and average <= 71:
    print("Your grade is b2")
elif average >= 51 and average <= 61:
    print("Your grade is c1")
elif average >=41 and average <= 51:
    print("Your grade is c2")
elif average >=31 and average <= 41:
    print("Your grade is d1")
elif average >=21 and average <= 31:
    print("Your grade is d2")
else:
    print("You failed")


