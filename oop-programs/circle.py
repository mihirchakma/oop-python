# Find the Area and Perimeter of the Circle using classes

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self.radius
    

# get radius input 
r = int(input("Enter radius of circle: "))

# create an object for Circle class 
obj = Circle(r)

print(f"Area of circle: {round(obj.area(), 2)}")
print(f"Perimeter of circle: {round(obj.perimeter(), 2)}")

