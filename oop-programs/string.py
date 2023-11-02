# Create a Class in which One Method Accepts a String from the User and Another Prints it

'''
Problem Solution:
1. Create a class and using a constructor initialize values of that class.
3. Create two methods called as get which takes in the value of a string and another called put that prints the string.
4. Create an object for the class.
5. Using the object, call both the methods.
6. The string is printed.
7. Exit
'''

class PrintString:
    def __init__(self):
        self.string = ""

    def get(self):
        self.string = input("Enter your string: ")

    def put(self):
        print(f"String is : {self.string}")

obj = PrintString()
obj.get()
obj.put()

'''
Program Explanation: 
1. A class called print1 is created and the __init__() method is used to initialize the value of the string to “”.
3. The first method, get, takes the value of the string from the user.
3. The second string, put, is used to print the value of the string.
5. An object for the class called obj is created.
6. Using the object, the methods get() and put() is printed.
7. The value of the string is printed.
'''