print("Please select your ride")
print("1. Bike")
print("2.Car")

choice = int(input("Please select your choice"))
if choice == 1 :
    print("What type of bike?")
    print("1. Scooty")
    print("2. Scooter")
 
    choice2  = int(input("Enter your choice"))
   
    if choice2 == 1 :
        print("You have selected scooty")
    else:
        print(" you have selected scooter ")
elif choice == 2 :
    print("What type of car?")
    print("1. Sedan")
    print("2. SUV")
 
    choice2  = int(input("Enter your choice"))
    if choice2 == 1 :
        print("You have selected sedan")
    else:
        print(" you have selected SUV")