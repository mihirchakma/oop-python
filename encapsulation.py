# Encapsulation 
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


single_book = Book('Deep Work', 1, 'Cal Newport', 200)

bulk_books = Book('Deep Work', 25, 'Cal Newport', 200)
bulk_books.set_discount(0.20)

print("Single Book Price: ", single_book.get_price())
print("Bulk Book Price: ", bulk_books.get_price())
print(single_book)
print(bulk_books) 