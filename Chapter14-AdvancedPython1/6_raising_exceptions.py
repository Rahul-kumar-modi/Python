a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(b == 0):
    raise ZeroDivisionError("Hey we can't divide number with zero")

else:
    print(f"The division a/b is {a/b}")