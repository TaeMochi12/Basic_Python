x=int(input("Enter the vale of x: "))
match x:
    case 0:
        print("x is 0")
    case 1:
        print("x is 1")
    case _ if(x<0):             #default case with condition
        print(x,"is negative")
    case _:
        print(x)
    