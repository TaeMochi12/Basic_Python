# we create custom errors so that if we want then , at some point the program shows an error and stop executing further
# it will prevent error in any further position of code because of the error present in the early lines only

a = int(input("Enter any value between 5 and 9:\n"))

if a < 5 or a > 9:
    raise ValueError("Value should be between 5 and 9")
