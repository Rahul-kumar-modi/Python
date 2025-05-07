class Employee:
    language = "Py" # This is class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry Ali" # This is object/instance attribute
print(harry.name, harry.language, harry.salary)

rohit = Employee()
rohit.name = "Rohit modi"
print(rohit.name, rohit.salary, rohit.language)

# Here name is object/instance attribute and salary and language are class attributes as they directly belong to the class