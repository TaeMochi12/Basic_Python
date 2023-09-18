def func():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index:"))
        print(l[i])
        return 1
    except:
        print("Some error occured")
        return 0

    finally:
        # it is always executed whether an error has occured or not
        print("I am always executed")
    # we could do this also and we might think that there is no need of finally but if the code is a part of a function then this will not execute but the finally clause always executes
    # print("I am always executed")


x = func()
print(x)
