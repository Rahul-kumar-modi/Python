s = {1, 5, 32, 34,5,2,5, "Sohail"}

print(s, type(s)) #o/p-> {32, 1, 34, 2, 5, 'Sohail'} <class 'set'>

s.add(6)
print(s) #o/p-> {32, 1, 34, 2, 5, 6, 'Sohail'}

s.remove(32)
print(s, type(s)) #o/p-> {1, 34, 2, 5, 6, 'Sohail'} <class 'set'>