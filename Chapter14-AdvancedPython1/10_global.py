a = 45 #global variable
def func():
    global a
    a = 3 #local variable
    print(a)

func() #o/p-> 3 if we add line 3 the o/p is same.
print(a) #o/p-> 45 if we add line 3 the o/p is 3.