class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color=color

    def start(self):
        print(f"{self.brand} {self.color} is starting----")

car1 = Car("Toyota","Red")
car2 = Car("Honda","Black")

print(car1.brand)
print(car2.brand)

print(car1.color)


car1.start()
car2.start()






# Parent class
class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.color} {self.brand} vehicle is starting...")

# Child class (Inheritance)
class Car(Vehicle):
    def start(self):  # Polymorphism: overriding the parent method
        print(f"{self.color} {self.brand} car is starting with a roar!")

# Another Child class
class Bike(Vehicle):
    def start(self):  # Polymorphism: overriding differently
        print(f"{self.color} {self.brand} bike is starting with a vroom!")

# Objects
car1 = Car("Toyota", "Red")
bike1 = Bike("Yamaha", "Blue")

# Accessing attributes and methods
print(car1.brand)   # Red
print(bike1.color)  # Blue

car1.start()        # Polymorphism in action
bike1.start()       # Polymorphism in action








# Functional style: data + functions

# Data for vehicles
car1 = {"type": "Car", "brand": "Toyota", "color": "Red"}
bike1 = {"type": "Bike", "brand": "Yamaha", "color": "Blue"}

# Function to "start" a vehicle
def start_vehicle(vehicle):
    if vehicle["type"] == "Car":
        print(f"{vehicle['color']} {vehicle['brand']} car is starting with a roar!")
    elif vehicle["type"] == "Bike":
        print(f"{vehicle['color']} {vehicle['brand']} bike is starting with a vroom!")
    else:
        print(f"{vehicle['color']} {vehicle['brand']} vehicle is starting...")

# Accessing attributes
print(car1["brand"])
print(bike1["color"])

# Calling functions
start_vehicle(car1)
start_vehicle(bike1)
