# public: by default all the members are public
# private: no strict concept of private, still can be a weak internal use indicator
#          by prefixing the member's name with double underscore __
#          can be accessed indirectly by using _classname (name      mangling- ek tarah se private member ka name change kr deta h ex: __name -> _Employee__name)
# protected: can be accessed within the class and subclass.. can be specified by prefixing member's name with an underscore _




# private access specifier-

class Employee:
    def __init__(self):
        self.__name="Himanshi"

a=Employee()
# print(a.__name)   #throws an error on directly accessing private member
print(a._Employee__name)

# protected access specifier-

class Emp:
    def __init__(self):
        self._name="Pratik"
    
    def _funshow(self):
        print("Name:",self._name)

class prgrmr(Emp):
    pass

a=Emp()
a1=prgrmr()
a._funshow()
a1._funshow()