class Demo:
    pass
d1=Demo()

class Employee:
    '''This is employee class for maintaining employee data'''
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(f'name is:{self.name} and age is {self.age}')
e1=Employee('usman',21)
e2=Employee('hamza',23)

print(isinstance(e1,Employee))
print(isinstance(d1,Demo))

if isinstance(obj,classname):
    pass

