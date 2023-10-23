# Method Overloading 
class OverloadingDemo:
    def add(self, x, y):
        print(x + y)

    def add(self, x, y, z):
        print(x + y + z)

obj = OverloadingDemo()
# obj.add(10, 20) # trow an error 
obj.add(10, 20, 30)