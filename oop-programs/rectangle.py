# Find the Area of a Rectangle Using Classes

'''
Problem Solution:

1. Take the value of length and breadth from the user.
2. Create a class and using a constructor initialise values of that class.
3. Create a method called as area and return the area of the class.
4. Create an object for the class.
5. Using the object, call the method area() with the parameters as the length and breadth taken from the user.
6. Print the area.
7. Exit
'''

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
l = int(input("Enter your length of rectangle: "))
b = int(input("Enter your breadth of rectangle: "))

obj = Rectangle(l, b)

print(f"Area of rectangle is {obj.area()}")


'''
Program Explanation:

1. User must enter the value of length and breadth.
2. A class called rectangle is created and the __init__() method is used to initialise values of that class.
3. A method called as area, returns self.length * self.breadth which is the area of the rectangle.
4. An object for the class is created.
5. Using the object, the method area() is called with the parameters as the length and breadth taken from the user.
6. The area is printed.
'''