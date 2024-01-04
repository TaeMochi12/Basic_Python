# 3 built-int functions used to get information about objects: dir(),dict, and help()

# dir() - The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object.

# dict - This attribute returns a dictionary representation of an object's attributes.

# help() - This function is used to get help documentation for an object, including a description of its attributes and methods.

# -- dir()
x=[1,2,3]       # this is a list
print(dir(x))   # this will give all the attributes and meethods that can be used with the above list
print(x.__add__)    # this will give info about the __add__ method if it exists otherwise it will throw a name error

# -- dict
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1


p = Person("John", 30)
# whichever attributes have self, they will be printed in a dictionary form using this attribute
print(p.__dict__)

# -- help()
print(help(Person))
