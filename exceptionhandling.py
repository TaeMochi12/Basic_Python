# if a string is entered instead of an integer then the program throws an error
a = input("Enter the number: ")
print(f"Multiplication Table of {a} is:")
try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:  # if we don't need e for printing then we just write... except:
    print(e)  # or we can print any other statement of our choice

print("End of program")

# We can handle a specific type of error as well as multiple types of error
try:
    num = int(input("Enter an integer: "))
    a = [2, 7]
    print(a[num])
except ValueError:
    # if the no. entered is not a valid integer
    num = print("Number entered is not an integer.")

except IndexError:
    # if no. entered is more than 1 as the list only has 0 and 1 indices
    print("Index Error")
