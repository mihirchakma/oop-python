# Append, Delete and Display Elements of a List using Classes 

'''
Problem Solution: 
1. Create a class and using a constructor initialize values of that class.
2. Create methods for adding, removing and displaying elements of the list and return the respective values.
3. Create an object for the class.
4. Using the object, call the respective function depending on the choice taken from the user.
5. Print the final list.
6. Exit
'''

class Check:
    def __init__(self):
        self.number = []

    def add(self, a):
        return self.number.append(a)
    
    def remove(self, b):
        self.number.remove(b)

    def display(self):
        return self.number

# creating an object for Check class 
obj = Check()

choice = 1

while choice != 4:
    print("1. Add")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        number = int(input("Enter a number to append: "))
        obj.add(number)
        print(f"List : {obj.display()}")
    elif choice == 2:
        number = int(input("Enter a number to remove: "))
        obj.remove(number)
        print(f"List : {obj.display()}")
    elif choice == 3:
        print(f"List : {obj.display()}")
    elif choice == 4:
        print("Exiting..!")
    else:
        print("Invalid choice.!")

print()


'''
Program Explanation:

1. A class called check is created and the __init__() method is used to initialize values of that class.
2. Methods for adding, removing and displaying elements of the list have been defined.
3. The menu is printed and the choice is taken from the user.
4. An object for the class is created.
5. Using the object, the respective method is called according to the choice taken from the user.
6. The final list is printed.
'''
