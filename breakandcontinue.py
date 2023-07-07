for i in range(11):
    if (i == 5):
        print("Skip maar diya :P")
        continue
    print(i)
    if (i == 8):
        break
print("Loop se bahar aa gye")


# DO WHILE LOOP EMALUATION IN PYTHON

i = 50
while True:
    # this part will run irrespective of the condition at least once in the beginning
    print(i)
    if (i % 100 == 0):  # condition check
        break
    i = i+1
