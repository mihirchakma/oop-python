# Create a Class and Get All Possible Distinct Subsets from a Set 

'''
Problem Solution: 

1. Create a class and define two methods in the class.
3. Method f1 is used to pass an empty list and the sorted list taken from the user to method f2.
4. Method f2 is used to compute all possible subsets of the list.
5. Then the result is returned from the function and printed.
6. Exit
'''

class Subsets:
    def f1(self, s1):
        return self.f2([], sorted(s1))
    
    def f2(self, current_value, s1):
        if s1:
            return self.f2(current_value, s1[1:]) + self.f2(current_value + [s1[0]], s1[1:])
        return [current_value]
    

a = [] 
number = int(input("Enter number of elements of list: "))
for i in range(0, number):
    b = int(input("Enter element: "))
    a.append(b)

print(f"Subsets: {Subsets().f1(a)}")

'''
Program Explanation: 

1. A class called sub is created and two methods f1 and f2 are defined.
3. In main, the number of elements is taken from the user.
3. Using a for loop, the elements are taken from the user and appended to an empty list.
5. Then, the method f1 of the class sub is called by passing the list taken from the user as the parameter.
6. Method f1 in turn calls method f2 with an empty list and the sorted list taken from the user as parameters.
7. Method f2 is a recursive function.
8. This method computes all the possible subsets by splitting the current list part by part starting from an empty list and updating the value of the current list.
9. This continues till the list becomes empty.
10. The current value of the list which is a list containing subsets as separate lists is returned.
11. The final result is printed.
'''
