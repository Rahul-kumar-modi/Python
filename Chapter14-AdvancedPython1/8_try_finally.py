# try:
#     a = int(input("Hey, Enter a number: "))
#     print(a)

# except Exception as e:
#     print(e)

# finally:
#     print("Hey I am inside of finally")

# print("Hey I am inside of finally")

#o/p -> line 8 with "finally" and line11 both print same o/p so why we use finally then we use it because finally comes in handy when we use in a function with return statement.


#Example->

def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey I am inside of finally") #If we use line11 on place finally then this will not print this because within try and except function return from it.

main()