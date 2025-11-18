class Employee:
    '''This is employee class for maintaining employee date'''
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f"name is:{self.name} and age is {self.age}")
e1=Employee('usman',23)
e1.display()


print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__class__)
print(Employee.__base__)
print(Employee.__dict__)