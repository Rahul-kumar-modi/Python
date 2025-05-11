def myFunc():
    print("Hello world!")

myFunc()
print(__name__) #o/p ->This will print "__main__" because we run module file itself.

if __name__ =="__main__":
    print("We are directly running the code")
    
