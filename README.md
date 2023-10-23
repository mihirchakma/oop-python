# Object Oriented Programming in Python

**Object-oriented programming (OOP)** in Python is a way of designing applications using **objects** and **classes**. Objects are self-contained entities that contain both data and behavior. Classes are **blueprints** for creating objects.

OOP is a powerful programming paradigm that can help you write more modular, reusable, and secure code. It is based on **Four Core** principles:

- **Encapsulation:** Encapsulation is the idea of wrapping data and the methods that work on data within one unit. This makes your code more secure and easier to maintain.

- **Inheritance:** Inheritance allows you to create new classes that inherit the data and behavior of existing classes. This can save you a lot of time and effort when developing new code.

- **Polymorphism:** Polymorphism allows you to write code that can work with different types of objects without having to change the code itself. This makes your code more flexible and reusable.

- **Abstraction:** Abstraction allows you to hide the internal implementation details of your objects and expose only the functionality that users need to know. This makes your code easier to understand and use.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        print("The car is driving.")

    def stop(self):
        print("The car has stopped.")

my_car = Car("Toyota", "Camry", 2023)

my_car.drive()
my_car.stop()

```

OOP is a powerful tool for developing complex and scalable applications in Python. By understanding the four core principles of OOP, you can write more modular, reusable, and secure code.

- Reference: [Object Oriented Programming](https://www.freecodecamp.org/news/object-oriented-programming-in-python/)
