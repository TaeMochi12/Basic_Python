a = 330
b = 3303
print("A") if a > b else print("=") if a == b else print("B")
# if there is nothing you wanna do in else then just write else with a blank double quote otherwise you'll get an error
print(9) if a > b else ""
# we can also write expressions
c = 9 if a < b else 0
print(c)
