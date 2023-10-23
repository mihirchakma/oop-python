# Abstraction
from abc import ABC, abstractmethod

class Book(ABC): # import ABC class 
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.__price = price # private attribute 
        self.__discount = None # private attribute 

    # setter method 
    def set_discount(self, discount):
        self.__discount = discount

    # getter method 
    def get_price(self):
        if self.__discount:
            return self.__price * (1 - self.__discount)
        return self.__price

    @abstractmethod # decorator 
    def __repr__(self) -> str:
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"


class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages 
    
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Pages: {self.pages}, Price: {self.get_price()}"


class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch 

    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}, Branch: {self.branch}"


# create objects 
novel1 = Novel('Deep Work', 10, 'Cal Newport', 200, 250)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 735, 'IT')

print(novel1)
print(academic1) 