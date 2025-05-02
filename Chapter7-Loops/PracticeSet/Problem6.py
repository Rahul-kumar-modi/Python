#Write a program to print * pattern like below and number is taken from user
'''
*****
*   *
*   *
*   *
***** (n==5)
'''
n = int(input("Enter the number: "))

# 1st method->
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print("*" * n)
#     else:
#         print("*" + " " * (n - 2) + "*")


#2nd method->
for i in range(1,n+1):
    if i == 1 or i == n:
        print("*" * n, end="")
    else:
        print("*", end="")
        print(" "* (n-2), end="")
        print("*", end="")
    print("")