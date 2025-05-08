class Employee:
    a = 1

    @classmethod  # If this class decorator given then "a" value taken from class attribute(a = 1). If not given then value "a" (a = 34) taken from instance attribute
    def show(cls): #In this we write "cls" instead "self" which is standard.
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 34

e.show()

# "self" is object on which method is running
# "cls" is class on which method is running