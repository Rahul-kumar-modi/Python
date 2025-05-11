#Printing the elements in list with index

l = [3, 513, 53,45]
#1st way:- with loop

# index = 0
# for item in l:
#     print(f"The item number at index {index} is {item}")
#     index += 1

#2nd way:- with enumerate function

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")