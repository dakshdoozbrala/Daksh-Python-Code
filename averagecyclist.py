a = int(input("Enter the value of first cyclist"))
b = int(input("Enter the value of second cyclist"))
c =int(input("Enter the value of third cyclist"))

average = (a+b+c)/3
print("The average is=",average)

if average > a and average > b and average > c :
    print("%d is higher than %d , %d , %d"%(average,a,b,c))
elif average > a and average > b:
    print("%d is higher than %d ,%d" %(average,a,b))
elif average > a and  average > c :
    print("%d is higher than %d , %d " %(average,a,c))
elif average > b and average > c:
    print("%d is higher than %d ,%d" %(average,a,c))
elif average > a :
    print("%d is higher than %d" %(average,a))
elif average > b :
    print("%d is higher than %d" %(average,b))
elif average > c :
    print("%d is higher than %d" %(average,c))
else:
    print("Invalid Input")