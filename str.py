string = input("Enter the string")
char = input("Enter the character:")

i = 0
count = 0

while(i < len(string)) :

    if(string[i] == char):
        count =count+1
    i = i+1 
print("The count is",count)

lower = int(input("Enter a lower number: "))
upper = int(input("Enter a upper number"))

print("The prime number between" ,lower, "and" ,upper, "are")

for num in range(lower,upper+1):

 if num > 1 :
    for i in range(2,num):
       if (num % i) == 0:
          break
    else:
        print(num)
 
num = input("Enter a number:")
length = len(num)

if length % 2 == 0:
   mid1 = int(num[length//2-1])
   mid2 = int(num[length//2])
   product = mid1*mid2
else:
   mid1 = int(num[length//2])
   product = mid1

print("The product of middle digits",product)