#Write a program to print a table in reverse.

n = int(input("Enter the number: "))

for i in range (1, 11):
    # print(f"{n} X {10-(i-1)} = {n*(10-(i-1))}") 
    print(f"{n} X {11-i} = {n*(11-i)}") 