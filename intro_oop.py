class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    # __repr__ is a special method used to represent a class’s objects as a string
    def __repr__(self) -> str:
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

book1 = Book('Book 1', 10, 'Author 1', 1500)
book3 = Book('Book 2', 10, 'Author 2', 2000)
book2 = Book('Book 3', 10, 'Author 3', 2500)

print(book1)
print(book2)
print(book3)