# medicalcause = input("Enter the Medical cause Y or N")
# attendance  = int(input("Enter the attendance"))
# if medicalcause == "yes" :
#     print ("yes you are allowed")
# else:
#     if attendance >= 75:
#         print("You are allowed")
#     else:
#         print("You are not allowed")




units = int(input("Enter the units for electricity bill"))

if units < 50:
    amount = units*2.60
    charges = 25
elif units <= 100 :
    amount = units*3.25+130
    charges = 35
elif units <= 200:
    amount = units*5.26+292
    charges = 45
else:
    amount = 130+162+526+(units*8.45)
    charges = 75
total = amount + charges
print(total)

