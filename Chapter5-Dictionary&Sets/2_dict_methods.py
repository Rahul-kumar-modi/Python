marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Modi"
}

print(len(marks)) #o/p-> 4
print(marks.items()) #o/p-> dict_items([('Harry', 100), ('Shubham', 56), ('Rohan', 23), (0, 'Modi')])

print(marks.keys()) #o/p-> dict_keys(['Harry', 'Shubham', 'Rohan', 0])

print(marks.values()) #o/p-> dict_values([100, 56, 23, 'Modi'])

# marks.update({"Harry": 99}) #o/p-> {'Harry': 99, 'Shubham': 56, 'Rohan': 23, 0: 'Modi'} because dictonary is mutable

marks.update({"Harry": 99, "Monika": 55}) 
print(marks) #o/p-> {'Harry': 99, 'Shubham': 56, 'Rohan': 23, 0: 'Modi', 'Monika': 55} because in dictonary is Monika will add

print(marks.get("Shivika")) #o/p-None
print(marks.get("Monika")) #o/p-> 55
print(marks["Monika"]) #o/p-> 55
print(marks.get("Rohit")) #o/p-> None
print(marks["Rohit"]) #o/p->Gives error


 
