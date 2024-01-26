class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("The name is", self.name)


class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print("The dance is", self.dance)


class DancerEmployee(Employee, Dancer):
    def __init__(self, name, dance):
        self.name = name
        self.dance = dance


o = DancerEmployee("Himanshi", "Kathak")
print(o.name)
o.show()  # it will execute the show method of the first inherited class i.e. Employee if it was DancerEmployee(Dancer,Employee) then the show of Dancer will be executed
# it shows the order in which classes will be searched first
print(DancerEmployee.mro())
