class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
e1=Employee('usman',23)
e2=Employee('hamza',24)

print(getattr(e1,'age'))
setattr(e1,'name','usman ashraf')

print(e1.__dict__)

delattr(e1,'age')

print(e1.__dict__)


print(hasattr(e1,'name'))