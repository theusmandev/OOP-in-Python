class Employee:
    def __init__(self):
       self.salary=30000
       self.age=20

e1=Employee()
e2=Employee()

print(e1.__dict__)
print(e1)





class Employee:
    def __init__(self):
        self.salary = 30000
        self.age = 20

    def __str__(self):
        return f"Employee(salary={self.salary}, age={self.age})"

e1 = Employee()
print(e1)





class Employee:
    def __init__(self,salary,age):
        self.salary=salary
        self.age=age

e1 = Employee(20000,22)
print(e1.__dict__)



class Employee:
    def __init__(self):
        pass

e1 = Employee()   # ✅ this creates an object




class Employee:
    def __init__(self):
        print("Constructor called")

e1 = Employee()






class Employee:
    # Default constructor
    def __init__(self):
        self.name = "Ali"
        self.salary = 30000

# Create objects
e1 = Employee()
e2 = Employee()

# Access attributes
print(e1.name, e1.salary)   # Ali 30000
print(e2.name, e2.salary)   # Ali 30000






class Employee:
    def set_data(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee()
e1.set_data("Ali", 30000)
print(e1.name, e1.salary)











class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, data_str):
        name, salary = data_str.split("-")
        return cls(name, int(salary))

e1 = Employee.from_string("Ali-30000")
print(e1.name, e1.salary)







class MyClass:
    def __new__(cls):
        print("Creating object")
        return super().__new__(cls)

    def __init__(self):
        print("Initializing object")

obj = MyClass()
