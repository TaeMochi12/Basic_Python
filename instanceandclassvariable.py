class Employee:
    companyName="Apple"         # here companyName is a class variable and it remains same and common for all instances
    noOfEmployees=0
    def __init__(self,name):
        self.name=name          # here name is an instance variable which is associated to the instance
        Employee.noOfEmployees+=1   #it will increase the no. of employees whenever a new employee will be made
    def show(self):
        print("Name:",self.name,"Company:",self.companyName,"Size:",self.noOfEmployees)

emp1=Employee("Himanshi")
emp2=Employee("Pratik")
emp1.companyName="Google"    #this will change company name for emp1 as if the instance variable is not found then class variable is searched and the change is made for emp1 only but not for the other objects
print(Employee.companyName)    #this will print apple
Employee.companyName="Nestle"   #this will change the companyName from Apple to Nestle and now the companyName for emp2 will also be changed

# These both i and ii are same:
emp1.show()         # i ...... it gets coverted to ii
# Employee.show(emp1) # ii

emp2.show()