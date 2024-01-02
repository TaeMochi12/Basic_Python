# static methods belong to a class rather than an instance of the class
# defined using @staticmethod decorator
# don't have access to the instance of the class (i.e. self)
# used to create utility functions that don't need access to instance data

class Math:
    def __init__(self,num):
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n

    @staticmethod
    def add(a,b):
        return a+b
    
a=Math(5)
print(a.num)
a.addtonum(6)
print(a.num)
print(Math.add(5,6))   #a.add(5,6) will also work although it doesn't have access to self