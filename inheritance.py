# Inheritance 
class Book:
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

    def __repr__(self) -> str:
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.get_price()}"

# inherited the Book superclass(parent) to Novel subclass(child) 
class Novel(Book):
    def __init__(self, title, quantity, author, price, pages):
        super().__init__(title, quantity, author, price)
        self.pages = pages

class Academic(Book):
    def __init__(self, title, quantity, author, price, branch):
        super().__init__(title, quantity, author, price)
        self.branch = branch


# create objects 
novel1 = Novel('Deep Work', 1, 'Cal Newport', 200, 250)
novel1.set_discount(0.20)

academic1 = Academic('Python Foundations', 12, 'PSF', 735, 'IT')

print(novel1)
print(academic1) 

print(novel1.pages)
print(academic1.branch)