# tuples are unchangeable(immutable)..tup[0]=90 can't be done
tup = (1, 4, 6, "Himanshi", True)
print(type(tup), tup)
print(tup[2])
print(tup[1:4])

# for tuple of 1 element a comma(,) is necessary otherwise type will be class int
tup2 = (2,)
print(type(tup2))
if 4 in tup:
    print("yes,it's present")
# tuple slicing will create new tuple here
tup3 = tup[1:5]
print(tup3)
