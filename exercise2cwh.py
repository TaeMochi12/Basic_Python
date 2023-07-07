import time
timenow = time.strftime("%H:%M:%S")
print(timenow)
name = input("Enter teacher's name: ")
hours = int(time.strftime('%H')) #similarly %M will give minutes and %S will give seconds.. also the hours minutes and seconds aren't in integer so we have to convert it into int for applying comparison methods
if (5 <= hours <= 11):
    print("Hello", name, "Good Morning!")
elif (12 <= hours <= 16):
    print("Hello", name, "Good Afternoon!")
elif (17 <= hours <= 20):
    print("Hello", name, "Good Evening!")
else:
    print("Hello", name, "Good Night!")
