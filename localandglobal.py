x=4  #global variable
print(x)

def hello():
    x=5    #local variable
    print(f"The local x is {x}")  #prints local x
    print("HELLOOO")

#To change global variable through func
def hello1():
    global x   #it means we are using global variable
    x=12


print(f"The global x is {x}")  #prints global x=4
hello()                         #this won't change global x
print(f"The global x is {x}")  #prints global x=4
hello1()        #this will change global x
print(f"The global x is {x}")  #prints global x=12