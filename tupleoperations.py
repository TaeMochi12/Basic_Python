# We cannot directly change a tuple, first convert it into a list then do the changes and then convert back to tuple
countries = ("India", "South Korea", "Norway", "Switzerland")
print(countries)
temp = list(countries)
temp.append("Japan")  # add item
temp.pop(0)  # remove item
temp[2] = "Scotland"  # change item
countries = tuple(temp)
print(countries)

# we can concatenate tuples directly to make a new tuple
countries2 = ("India", "Switzerland", "Maldives")
visit = countries+countries2
print(visit)

# Tuple methods

tup = (4, 1, 4, 7, 4, 9, 4, 6)
# counts the no. of occurences of a particular item
print('Count of 4 in tuple is:', tup.count(4))
# returns the first occurence  of the given element from the tuple..raises a ValueError if the element is not found
print(tup.index(9))
# firstly string slicing will be performed 1:6 then 4's first occurence index will be printed from that part
print(tup.index(4, 1, 6))

print(len(tup))
