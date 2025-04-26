c = 32
x = type(c)
print(x) #Give output:- <class 'int'>

d = 32.8
y = type(d)
print(y) #Give output:- <class 'float'>

d = "Rupesh"
z = type(d)
print(z) #Give output:- <class 'str'>

e = "32.8"
t = type(e)
print(t) #Give output:- <class 'str'>

f = "32.8"
g = float(f) # f type is string but we typecast "f" into float in "g"
s = type(g)
print(s) #Give output:- <class 'float'>

