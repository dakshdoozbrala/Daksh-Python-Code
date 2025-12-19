# storing the values
tree1 = 98
tree2 = 91
tree3 = 41
tree4 = 95
tree5= 11

sum = tree1+tree2+tree3+tree4+tree5
print("The sum of the trees is",sum)

average = sum/5
print("The Average of the trees is",average)

Amount= int(input("Please enter the amount for withdrew"))

note_1= Amount//100
note_2=(Amount%100)//50
note_3=((Amount%100)%50)//10

print("The Amount of 100 rupee note is",note_1)
print("The Amount of 50 rupee note is",note_2)
print("The Amount of 10 rupee note is",note_3)

english = int(input("English:"))
maths = int(input("Maths:"))
science=int(input("Science:"))
hindi=int(input("Hindi:"))

sum = english+hindi+maths+science
print("Total Marks are",sum)

percentage=(sum/400)*100
print("The percentage of the numbers is",percentage)

days = int(input("Enter the number of days:"))

years = days//365
remaining_days = days%365
week = remaining_days//7
final_underscoredays= remaining_days%7

print("No of years remaining",years)
print("No of days remaining",remaining_days)
print("Days in a week remaining",week)
print("Final days:",final_underscoredays)

year = int(input("Enter the year:"))
if year%400 == 0:
        print("This is a leap year") 
elif year%100 == 0:
        print("This is not a leap year")
elif year%4 == 0:
        print("This is a leap year")
else:
        print("Not a leap year")