# Operator Overloading is a feature in python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types(objects).
# You can use standard mathematical and comparison operators in your own classes, just as you would for built-in data types like int,float and str.

class Vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
    
    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"
    
    def __add__(self,x):
        # return f"{self.i+x.i}i+{self.j+x.j}j+{self.k+x.k}k"  -> this will return a string after addition but we want a vector after adding two vectors that's why did like below
        return Vector(self.i+x.i,self.j+x.j,self.k+x.k)
    
v1=Vector(3,5,6)
print(v1)

v2=Vector(2,5,7)
print(v2)

print(v1+v2)   # self is v1 and x is v2
print(type(v1+v2))
 