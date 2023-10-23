# Method Overriding 
class ParentClass:
    def call_me(self):
        print('I am parent class')

class ChildClass(ParentClass):
    def call_me(self):
        print('I am child class')
        super().call_me() # overriding with super class 

pobj = ParentClass()
pobj.call_me()

cobj = ChildClass()
cobj.call_me()