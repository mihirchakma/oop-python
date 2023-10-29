"""
Problem Solution:

1. Create a class and using a constructor to initialize values of that class.
2. Create methods for adding, substracting, multiplying and dividing two numbers and returning the respective results.
3. Take the two numbers as inputs and create an object for the class passing the two numbers as parameters to the class.
4. Using the object, call the respective function depending on the choice taken from the user.
5. Print the final result.
6. Exit
"""

class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2 
    def sub(self):
        return self.num1 - self.num2 
    def mul(self):
        return self.num1 * self.num2 
    def div(self):
        return self.num1 / self.num2 
    
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

# create an class object 
obj = calculator(a, b)

choice = 1

# while loop 
while choice != 0:
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("0. Exit")

    # choice selection with if-else condition 
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print(f"Result: {obj.add()}\n")
    elif choice == 2:
        print(f"Result: {obj.sub()}\n")
    elif choice == 3:
        print(f"Result: {obj.mul()}\n")
    elif choice == 4:
        print(f"Result: {obj.div()}\n")
    elif choice == 0:
        print("Exiting!")
    else:
        print("Invalid choice!")

print("---------------------")

"""
Program Explanation:

1. A class called calculator is created and the __init__() method is used to initialize values of that class.
2. Methods for adding, substracting, multiplying, dividing two numbers and returning their respective results is defined.
3. The menu is printed and the choice is taken from the user.
4. An object for the class is created with the two numbers taken from the user passed as parameters.
5. Using the object, the respective method is called according to the choice taken from the user.
6. When the choice is 0, the loop is exited.
7. The final result is printed.
"""
