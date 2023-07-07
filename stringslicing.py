name = "Himanshi"

# it will print from 0 to 3rd index(not 4th index),also [0:4] is same as [:4]
print(name[0:4])
# it will print from 4 to 7th index(not 8th index),also [4:8] is same as [4:]
print(name[4:8])
# it will print from 3rd to 4th index(not 5th index),it works like [n-5:n-3] where n is no. of elements
print(name[-5:-3])
print(name[-5:])
print(name[:-5])
print(name[-3:-5])  # this won't work
