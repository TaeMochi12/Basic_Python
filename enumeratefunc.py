marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if (index == 3):
#         print("Himanshi, Awesome!")
#     index += 1

# We can do the above task without writing this much
# Using enumerate function, we can get the index and value of each element in the sequence at the same time

# we can also change starting index
for index, mark in enumerate(marks, start=1):
    print(mark)
    if (index == 3):
        print("Himanshi, Awesome!")

for v in enumerate(marks):  #if prints the index and value pair in form of tuple
    print(v)
