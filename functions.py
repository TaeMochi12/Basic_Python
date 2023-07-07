def CalcAvg(a, b):
    avg = (a+b)/2
    print(avg)


def grtno(a, b):
    if (a > b):
        print(a, "is greater")
    else:
        print(b, "is greater or equal")


CalcAvg(2, 4)
grtno(8, 8)


def haha(c, d):
    pass  # if we want to define function later on so this will not create any hinderance in smoothly running program

# we can also call a function in another function


def grtandavg(a, b):
    CalcAvg(a, b)
    grtno(a, b)


grtandavg(2, 7)


# passing default arg
def avg(a=1, b=3):
    print("avg= ", (a+b)/2)


avg()
avg(3, 5)
avg(b=2)

# arguments can be passed in any order(keyword arguments)
avg(b=4, a=3)

# required arguments, if any default argument isn't given then we are required to pass an argument for that keyword

# Variable  length arguments


def average(*numbers):  # it took numbers as tuple
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average is: ", sum/len(numbers))
    # print(numbers) ... using this tuple will be printed


average(1, 2, 3, 4)


def name(**name):  # takes name as dictionary
    print("Hello,", name["fname"], name["mname"], name["lname"])
    # print(name) .. prints dictionary


name(lname="Sharma", fname="Anil", mname="Kumar")

#return statement
def sum(a, b):
    sum = a+b
    return sum


c = sum(2, 8)
print(c)
print(sum(4, 6))
