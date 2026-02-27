#create a class person with private attributes_name and _age
#use getter and setter methods to access and modify these attributes
class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self._age = age     # Protected attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self._age

    # Setter for age
    def set_age(self, age):
        self._age = age

"""create a function show_details(obj) that works with different classes
define the same method name (details()) in two or more classes and show how show_details can call the method for different objects
call show_details() with different objects to show polymorphism in action"""
def show_details(obj):
    obj.details()
    name = obj.get_name() if hasattr(obj, 'get_name') else "Unknown"
    print(f"Name: {name}")
called_objects = []
class Student:
    def __init__(self, name, grade):
        self.__name = name
        self.grade = grade

    def details(self):
        print(f"Student Grade: {self.grade}")

    def get_name(self):
        return self.__name
    
"""
Create a base class Vehicle with a method start().
Create a derived class Bike that inherits from Vehicle.
Bike should have its own method wheels() that prints "Two wheels".""" 
class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Bike(Vehicle):
    def wheels(self):
        print("Two wheels") 

"""
Create class Singer with method sing() and class Dancer with method dance().
•	Create a class Performer that inherits from both.
•	Create a Performer object and call both methods
"""        
class Singer:
    def sing(self):
        print("Singer is singing")

class Dancer:
    def dance(self):
        print("Dancer is dancing")

class Performer(Singer, Dancer):
    pass

performer = Performer()
performer.sing()  # Output: Singer is singing
performer.dance()  # Output: Dancer is dancing

"""
Create a base class Appliance.
•	Create two child classes: WashingMachine and Microwave.
•	WashingMachine should have a method wash(), and Microwave should have a method heat().
•	Create objects of both and call their respective methods.
"""
class Appliance:
    pass
class WashingMachine(Appliance):
    def wash(self):
        print("Washing machine is washing clothes")
class Microwave(Appliance):
    def heat(self):
        print("Microwave is heating food")
washing_machine = WashingMachine()
microwave = Microwave()
washing_machine.wash()  # Output: Washing machine is washing clothes
microwave.heat()  # Output: Microwave is heating food
