# combination of key value pairs
# can be used for mapping
# dictionaries are ordered
dic = {
    "Himanshi": "A Girl",
    "Laptop": "Object"
}
# they will print the corresponding value of the key but there is a slight difference between them
print(dic["Himanshi"])  # this will throw an error if the key is not present
print(dic.get('Himanshi'))  # this will print None but not an error

# Accesing multiple values
print(dic.keys())
print(dic.values())

for key in dic.keys():
    print(f"The value corresponding to the key {key} is {dic[key]}")

print(dic.items())  # key and value pairs are obtained in the form of tuples

for key, value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")
