s1 = {1, 2, 4, 6}
s2 = {6, 7, 9, 8}
print(s1.union(s2))  # after this s1 and s2 still remain same
# this will update s1 as now it will have those elements from s2 which weren't already present in it
# s1.update(s2)
print(s1, s2)

print(s1.intersection(s2))
# this will update s1 as now it will have those elements which were present in both s1 and s2
# s1.intersection_update(s2)
print(s1, s2)

# SYMMETRIC DIFFERENCE=union-intersection
print(s1.symmetric_difference(s2))
# this will update s1 according to symmetric difference
# s1.symmetric_difference_update(s2)
print(s1, s2)

# SET DIFFERENCE=set1-set2
print(s1.difference(s2))
# this will update s1 according to difference
# s1.difference_update(s2)
print(s1, s2)

print(s1.isdisjoint(s2))  # checks if the sets are disjoint
# checks if the first set is the superset of the second set
print(s1.issuperset(s2))
print(s1.issubset(s2))  # checks if the first set is the subset of the second set

s1.add(69)
print(s1)

s1.update(s2)
print(s1)

# remove() and discard()
# main difference between remove and discard is that if the element is not present in the set which you want to delete then remove() will throw an error but discard won't
s1.remove(1)
print(s1)

# pop():removes a random value from the set
print(s2)
item = s2.pop()
print(s2)
print(item)

if 9 in s2:
    print("present")

s2.clear()  # it doesn't delete the set but all the set items
print(s2)


del s1  # it is a keyword..deletes the entire set
print(s1)
