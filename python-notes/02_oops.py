# Python OOP Basics - Sep 5, 2025

# Defining a simple class
class Person:
    def __init__(self, name, age):   # constructor
        self.name = name
        self.age = age

    def greet(self):  # instance method
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating objects (instances)
p1 = Person("Alice", 25)
p2 = Person("Bob", 30)

print(p1.greet())
print(p2.greet())

# Class with default values and method
class Circle:
    pi = 3.14159  # class attribute

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def circumference(self):
        return 2 * Circle.pi * self.radius

c1 = Circle(5)
print("Area:", c1.area())
print("Circumference:", c1.circumference())

# Inheritance (child class extending parent class)
class Animal:
    def speak(self):
        return "Some generic sound"

class Dog(Animal):   # inherits from Animal
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog()
cat = Cat()
print("Dog says:", dog.speak())
print("Cat says:", cat.speak())

# Special methods (__str__ for printing)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):   # defines how object is printed
        return f"'{self.title}' by {self.author}"

b = Book("1984", "George Orwell")
print(b)
