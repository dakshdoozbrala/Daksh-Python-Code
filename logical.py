# Usage of and operator to check if the values are true
a = 20 
b = 20

if a > 0 and b > 0 :
    print("20 is greater than 0")


# Usage of or operator
x = 30
y = 30
 
if x < 40 or y > 40:
   print("30 is less than 40 and not greater than 40")
else:
    print("30 is greater than 40 and not less than 40")

c = 10
d = 12
e = 12
 
print(c!=d)

print(d!=e)

weight = float(input("Enter your weight in kg:"))
height = float(input("Enter your height in cm"))

BMI = weight/(height/100)**2

if BMI <= 18.5 :
    print("You are underweight")
elif BMI <= 24.9:
    print("You are a Healthy Person")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are severely Overweight")
elif BMI <= 39.9 :
    print("You are obese")
else:
    print("You are severly obese")


