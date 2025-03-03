# Task 1: Lambda function to merge two lists into a dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
merge_lists = lambda keys, values: dict(zip(keys, values))
print("Merged Dictionary:", merge_lists(keys, values))

# Task 2: Create a class Product with instance variables and method to calculate discounted price
class Product:
    discount_rate = 0.1  # Class variable

    def __init__(self, name, price):
        self.name = name  # Instance variable
        self.price = price  # Instance variable

    def calculate_discounted_price(self):
        return self.price - (self.price * Product.discount_rate)

product = Product("Laptop", 1000)
print(f"Discounted price of {product.name}: {product.calculate_discounted_price()}")

# Task 3: Base class Shape and derived classes Circle and Rectangle (Inheritance)
class Shape:
    def area(self):
        pass  # This will be overridden by subclasses

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

circle = Circle(5)
rectangle = Rectangle(4, 6)
print(f"Area of Circle: {circle.area()}")
print(f"Area of Rectangle: {rectangle.area()}")

# Task 4: Multiple Inheritance with Person, Employee, and Manager classes
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def get_employee_id(self):
        return self.employee_id

class Manager(Person, Employee):
    def __init__(self, name, employee_id, department):
        Person.__init__(self, name)
        Employee.__init__(self, employee_id)
        self.department = department

    def get_manager_info(self):
        return f"Manager {self.name}, ID: {self.employee_id}, Department: {self.department}"

manager = Manager("Alice", 12345, "HR")
print(manager.get_manager_info())

# Task 5: Polymorphism - play_sound function accepting different animal objects
class Dog:
    def make_sound(self):
        return "Bark"

class Cat:
    def make_sound(self):
        return "Meow"

class Cow:
    def make_sound(self):
        return "Moo"

def play_sound(animal):
    print(animal.make_sound())

dog = Dog()
cat = Cat()
cow = Cow()

play_sound(dog)  # Outputs: Bark
play_sound(cat)  # Outputs: Meow
play_sound(cow)  # Outputs: Moo

# Task 6: Car Rental System with Vehicle, Car, and Bike classes
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, car_type):
        super().__init__(make, model, year)
        self.car_type = car_type  # Specific to Car

    def display_info(self):
        return f"Car: {super().display_info()} - Type: {self.car_type}"

class Bike(Vehicle):
    def __init__(self, make, model, year, bike_type):
        super().__init__(make, model, year)
        self.bike_type = bike_type  # Specific to Bike

    def display_info(self):
        return f"Bike: {super().display_info()} - Type: {self.bike_type}"

# Creating objects
car = Car("Toyota", "Corolla", 2022, "Sedan")
bike = Bike("Yamaha", "FZ", 2021, "Sports")

print(car.display_info())  # Outputs: Car: 2022 Toyota Corolla - Type: Sedan
print(bike.display_info())  # Outputs: Bike: 2021 Yamaha FZ - Type: Sports
