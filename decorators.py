# A decorator is a function that takes another function as an argument and returns a new function that modifies the behaviour of the orginal function
# it extends the functionality of a function or method without modifying its source code
# we could also do the changes in the original function but if we want to extend the functionality of more than 1 functions in the same way then it becomes easy using decorators
# the new modified function is referred to as "decorated" function

def greet(fx):      #decorator function
    def mfx(*args,**kwargs):   #if there are some arguments to be passed then we pass them like this in decorators : *args takes parameters in the form of tuple and **kwargs take the parameters in the form of dictionary key value pairs
        print("Hello")
        fx(*args,**kwargs)     #if we don't write args and kwargs then there is no use of passing 1 and 2 during call because here the function won't accept any arguments
        print("Thanks for using this function")
    return mfx

@greet          #this notation is just a short hand for this(see the commented function call of the function below)
def hie():
    print("Happy New Year!")

hie()
# greet(hie)()    #->this

@greet
def add(a,b):
    print(a+b)

add(1,2)
# greet(add)(1,2)
