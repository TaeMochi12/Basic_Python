class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def showDetails(self):
        print("The name of employee",self.id,"is",self.name)

class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")



e=Employee("Himanshi",12)
e.showDetails()

e2=Programmer("Pratik",18)
e2.showLanguage()
e2.showDetails()

# class Emp:
#     def __init__(self):
#         self.name="Himanshi"

#     def show(self):
#         print("Name",self.name)

# class Prgrmr(Emp):
#     def showlang(self):
#         print("Language:Python")

# e=Prgrmr()
# e.showlang()
# e.show()