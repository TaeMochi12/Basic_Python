# The class methods are bound to the class, not to the instance. It can modify the class state means it can change class configuration globally. It can access only the class variable. The class methods are used to create the factory methods. The syntax of class methods is different; instead of taking self parameter, they accept cls as a parameter that points to the class. It can't modify the instance state. However, the changes made by the class method reflect all instances of the class.



# class methods are used to change and modify the class variables
# it has access to the class rather than instance
# @classmethod decorator is used 

class Employee:
    company='Apple'     #class variable
    def show(self):
        print("The name is",self.name,"and company is",self.company)

    @classmethod
    def changeCompany(cls,newCompany):  #here we can write anything other than cls also, class will be passed as argument  
        cls.company=newCompany

e1=Employee()
e1.name="Himanshi"
e1.show()
e1.changeCompany('Tesla')   # if the @classmethod decorator isn't used then this will change the company name only for the e1 instance but now it will change the company name for the whole class and all its instances 
e1.show()
e2=Employee()
e2.name="Pratik"
e2.show()
print(Employee.company)