# a = int(input("Enter your age: "))
# print("Ohh so your age is:", a, ",then:")
# if (a >= 18):
#     print("Yay!You can drive!!")
# else:
#     print("Oops!You cannot drive")


# ans = input("Are you a BTS ARMY?? \n")

# if (ans == 'Yes'):
#     print("Yeah!")
# elif (ans == 'Maybe'):
#     print("Ohkay cool!")
# else:
#     print("Okay bye!")

num = int(input('Enter a number: '))
if (num > 0):
    print("No. is positive")
    if (num > 12):
        print("Also greater than 12")
    elif (num == 12):
        print("Number is equal to 12")
    else:
        print("But smaller than 12")

elif (num == 0):
    print("Number is zero")

else:
    print("Number is negative")
    if (num <= -12):
        print("And less than or equal to -12")
    else:
        print("But greater than -12")
