class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num): # Without it we cannot perform addition between n and m.
        return self.n + num.n
    
    def __sub__(self, num): # Without it we cannot perform addition between n and m.
        return self.n - num.n
    
n = Number(1)
m = Number(2)

print(n + m) #This give error because in python everything is class that why we get let example:- a = 4.0 then type(a) is <class, 'float'> in this format so performing addition operation in line 11 then we use "operator overloading" in line 5 and 6

print(n - m)