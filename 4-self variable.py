class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
#     def show(self):
#         print('Name:',self.name)
#         print('Salary:',self.salary)
# e1 = Employee("Ali",30000)
# e1.show()
e1 = Employee("Ali",30000)

print(e1.__dict__)
print(e1.name)








class student:
    def __init__(myobj,name):
        myobj.name= name
s1 = student("ali")
print(s1.name)










class Employee:
    def __init__(self, name, salary):
        self.name = name        # instance variable
        self.salary = salary    # instance variable

e1 = Employee("Ali", 30000)
e2 = Employee("Sara", 40000)

print(e1.name, e1.salary)   # Ali 30000
print(e2.name, e2.salary)   # Sara 40000







class Employee:
    company = "ABC Ltd"   # class variable

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Ali", 30000)
e2 = Employee("Sara", 40000)

print(e1.company)   # ABC Ltd
print(e2.company)   # ABC Ltd







class Employee:
    company = "ABC Ltd"   # class variable

    def __init__(self, name, salary):
        self.name = name  # instance variable
        self.salary = salary

e1 = Employee("Ali", 30000)
e2 = Employee("Sara", 40000)

Employee.company = "XYZ Pvt Ltd"

print(e1.company)  # XYZ Pvt Ltd (shared)
print(e2.company)  # XYZ Pvt Ltd (shared)
print(e1.name)     # Ali (unique)
print(e2.name)     # Sara (unique)












class Car:
    wheels = 4        # Line 1
    def __init__(self, brand, color):
        self.brand = brand   # Line 2
        self.color = color   # Line 3

c1 = Car("Toyota", "Red")
c2 = Car("Honda", "Blue")

c1.color = "Black"
Car.wheels = 6

print(c1.brand, c1.color, c1.wheels)
print(c2.brand, c2.color, c2.wheels)




class Car:
    wheels = 4        
    def __init__(self, brand, color):
        self.brand = brand   
        self.color = color   

c1 = Car("Toyota", "Red")
c2 = Car("Honda", "Blue")

c1.color = "Black"
c1.wheels = 8   # ⚡ This creates an instance variable for c1 only
Car.wheels = 6  # update class variable

print(c1.brand, c1.color, c1.wheels)
print(c2.brand, c2.color, c2.wheels)
