#a = (1,2,5,6) #o/p-> <class 'tuple'>
# a = ()  #o/p-> <class 'tuple'>
# a = (1) #o/p-> <class 'int'>
a = (1,) #o/p-> <class 'tuple'>
print(type(a)) 

b = (1,23,False,"Shivam","Satyam",34,4.68)
# b[0] =453 #Tuple is immutable just like strings so this give error

n = b.count(23)
print(n) #o/p-> 1

i = b.index(34)
print(i) #o/p -> 5
