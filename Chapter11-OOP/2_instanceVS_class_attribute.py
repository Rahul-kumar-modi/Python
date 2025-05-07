class Employee:
    language = "Python" # This is class attribute
    salary = 1200000 # This is class attribute

harry = Employee()
harry.language = "Javascript" # This is object/instance attribute
print(harry.language, harry.salary) #o/p-> "Javascript 1200000" if line 6 not given then o/p is Python on place of Javascript

#instance attribute take preference over class attribute during assignment & retrieval