class Person:
    
    # def __init__(self):         #default constructor:it always returns null
    #        print("Hey I am person")
    
    def __init__(self,n,o):         #parameterized constructor:it always returns null
           print("Hey I am person")
           self.name=n
           self.occ=o

    def info(self):
          print(f"{self.name} is a {self.occ}")

a=Person("Harry","Developer")
b=Person("Divya","HR")
a.info()
b.info()
