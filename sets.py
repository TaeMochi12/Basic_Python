# sets are unordered,unchangeable and they don't contain duplicate values
s = {2, 4, 2, 6}  # the items never follow an order..output can be in any order
print(s)  # it prints 2 one tym only
# sets can't be accessed using index numbers
info = {"Himanshi", 19, True, 5.4, 19}
print(info)

empty = set()  # if we do {} then it will create an empty dictionary not an empty set
print(type(empty))

# accessing set items

for i in info:
    print(i)
