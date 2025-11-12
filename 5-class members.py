

class student:
    school = "city high"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name,self.age,student.school)
s1 = student("Ali", 18)
s1.show()
