# Write a program to print multiplication table of a given number using for loop

n = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{n} X {i} = {n * i}")

#o/p-> 
#Enter a number: 6
# 6 X 1 = 6
# 6 X 2 = 12
# 6 X 3 = 18
# 6 X 4 = 24
# 6 X 5 = 30
# 6 X 6 = 36
# 6 X 7 = 42
# 6 X 8 = 48
# 6 X 9 = 54
# 6 X 10 = 60