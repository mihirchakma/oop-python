# Implementing Decorators within classes 

class MyClass:
    @staticmethod
    def method():
        return 'Static Method called'
    
    @classmethod
    def class_method(cls):
        return 'Class Method called'
    

print(MyClass.method())
print(MyClass.class_method())
