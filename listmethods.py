l = [12, 14, 8, 0, 2, 1, 2, 3, 4]
print(l)
# l.append(6)

# l.reverse()

# l.sort()

# l.sort(reverse=True)

# print(l.index(1))   #telling index of first occurence of 1

# print(l.count(2)) #no. of times 2 is coming

# m=l
# m[0]=0 #this will make change in l also.. not a recommended method to make a new list because m is the reference of l not its copy

# use copy method
# m = l.copy()
# m[0] = 0
# print(m)

# l.insert(2, 48) #this will insert 48 at the second index
n = [100, 1200, 1400]
# l.extend(n) #this will change l

k = l+n  # this will make a new list by concatenation
print(k)
print(l)
