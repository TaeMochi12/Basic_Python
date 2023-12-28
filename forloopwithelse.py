# else can also be used with while loop
for i in range(5):
    print(i)

else:  # when control is unable to go inside for loop
    print("Sorry,no i")

for i in range(6):
    print(i)
    if (i == 3):
        break

else:           # it will not run when the loop breaks.. it runs    when the loop successfully ends
    print("oops")

i = 0
while i < 7:
    print(i)
    i = i+1

else:
    print("sorry")

# just an example using string formatting
for x in range(5):
    print("iteration no {} in for loop".format(x+1))

else:
    print("else block in loop")
print("out of loop")
