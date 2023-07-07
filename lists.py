l = [12, 8, 14, "Himanshi", True]
print(l)
print(l[:])
print(l[:5])
print(type(l))
print(l[1])
print(l[-2])

if 10 in l:
    print("yes")
else:
    print("no")

if "12" in l:
    print("yes")
else:
    print("no")  # no will be printed because 12 is  as an integer in l

if "iman" in "Himanshi":  # same applies for strings as well
    print("yes")
else:
    print("no")

if "man" in l[3]:
    print("yes")
else:
    print("no")

# slicing is same as string slicing..jump index is also

# LIST COMPREHENSION.. Making list on the fly
lst = [i*i for i in range(5)]
print(lst)
lst2 = [i*i for i in range(10) if i % 2 == 0]
print(lst2)

names = [name for name in ["Himanshi", "Pragya", "Palak"] if name[0] == "P"]
print(names)
