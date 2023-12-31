class Person:
    name="Himanshi"
    occupation="Data Scientist"
    networth=80
    def info(self):   #self ka mtlb wo object jiske liye ye method call ho rha h
        print(f"{self.name} is a {self.occupation}")

a=Person()
b=Person()
a.name="Pratik"
a.occupation="CEO"
print(a.name,a.occupation,a.networth)
a.info()

b.name="Palak"
b.occupation="PO"
print(b.name,b.occupation,b.networth)
b.info()