class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    #it is acting as an alternative constructor by initialising the data members but using different data format
    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))  #here the string is split into different elements separated by - and the elements are returned in the form of a list
    

e1=Employee("Himanshi",1200000)
print(e1.name)
print(e1.salary)

string="Pratik-3400000"
e2=Employee.fromStr(string)     #if we didn't make the classmethod then we had to write it like this -> e2=Employee(string.split("-")[0],int(string.split("-")[1]))

print(e2.name)
print(e2.salary)
