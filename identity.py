a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = a
print(a is c)
print(a is b)
print(a is not c)
print(a is not b)

x = 5
if (type(x)is int):
    print("True")
else:
    print("False")

y = 3.5
if (type(y)is not float):
    print("True")
else:
    print("false")

x = 30
y = 30
if x is not y:
    print("true")
else:
    print("false")
