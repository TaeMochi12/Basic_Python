# -> The super() keyword is used to refer to the parent class.
# -> It is especially useful when a class inherits from multiple parent classes and you want to call a method from one of the parent classes.
# -> When a class inherits from a parent class, it can override or extend the methods defined in the parent class.
# -> Sometimes, you might want to use the parent class method in the child class, then we use super() keyword

class ParentClass:
    def parent_method(self):
        print("This is the parent method.")
        
class ChildClass(ParentClass):
    def parent_method(self):
        print("Himanshi")
        super().parent_method()     # when the child object calls parent_method then after the parent method of child class, this will call the prent method of parent class also
    def child_method(self):
        print("This is the child method.")

child_object=ChildClass()
child_object.child_method()
child_object.parent_method()

# CAN BE USED FOR CALLING THE PARENT CLASS CONSTRUCTOR ALSO

class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)   # instead of initialising the name and id again, we called the employee class constructor
        self.lang=lang

himanshi=Employee("himanshi",1214)
pratik=Programmer("pratik",1218,"Java")
print(pratik.name)

