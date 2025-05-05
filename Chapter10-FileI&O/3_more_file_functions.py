f = open("file.txt")

# lines = f.readlines()
# print(lines, type(lines)) #o/p-> ['Rahul is good coder\n', 'I am good boy\n', 'This is amazing'] <class 'list'>

# 1st way to print single line from "file.txt"
# line1 = f.readline()      #o/p-> Rahul is good coder
# print(line1, type(line1))  #    <class 'str'>


# line2 = f.readline()     #o/p-> I am good boy
# print(line2, type(line2)) # <class 'str'>

# line3 = f.readline()  #o/p-> This is amazing <class 'str'>
# print(line3, type(line3))

# line4 = f.readline()  #o/p-> <class 'str'>
# print(line4, type(line4))
# f.close()

# 2nd way to print single line from "file.txt"
line = f.readline()
while(line !=""): 
    print(line, type(line)) #o/p->  Rahul is good coder
    line = f.readline()     #       <class 'str'>
                            #       I am good boy
f.close()                   #       <class 'str'>
                            #       This is amazing <class 'str'>
