name = "!!Himanshi! Himanshi !!!"
# strings are immutable i.e. on applying string methods,the orginal string is not changed,a copy of string is made by the string methods
print(len(name))
print(name.upper())
print(name.lower())
# removes trailing characters,not the ones in the beginning
print(name.rstrip('!'))
# will replace all occurences of Himanshi with Hahaha
print(name.replace("Himanshi", "Hahaha"))
print(name.split(" "))  # will make a list of all parts separated by space
heading = "introduction tO pyTHon"
# Capitalizes the first character of the string to uppercase and the rest of the characters to lowercase
print(heading.capitalize())

str = "Welcome To The Console!!!"
print(str.center(50))  # aligns string to the center as per the parameter given
print(len(str))
print(len(str.center(50)))  # added 25 spaces in starting
print(name.count("Himanshi"))
print(str.endswith("!!!"))  # checks if the string ends with a given value
# we can also check for a value in-between the strings by providing start and end index positions
print(str.endswith("to", 4, 10))

str1 = "He's hungry.He is an honest man."
# find returns the first occurence of the given value and returns its index and returns -1 if not found
print(str1.find("is"))
# index is same as find but it throws an error if the value is not found
# print(str1.index("ish"))

# isalnum() returns truew if the string is made up of A-Z,a-z or 0-9
print(str.isalnum())
str2 = "HiMyNameIsHimanshi12"
print(str2.isalnum())
# islpha() returns true only if it contains a-z or A-Z .. if it contains numbers from 0-9 then it returns false
print(str2.isalpha())

print(str.islower())
str3 = "Merry christmas"
str4 = "Welcome\n"
# isprintable() returns true if all charcters are printable bu tin case of characters such as \n it will return false as if we print str4 then \n will not be printed just a new line is there in output
print(str4)
print(str3.isprintable())
print(str4.isprintable())
str5 = "              "
print(str5.isspace())  # returns true only if string contains white spaces

# returns true if the first letter of each word is capitalized
print(str.istitle())

print(str.isupper())

print(str.startswith('Welcome'))

print(str.swapcase())  # changes upper case to lower and lower case to upper

# makes the string a title i.e. first letter of each word is capitalized
print(heading.title())
