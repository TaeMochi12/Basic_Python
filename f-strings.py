Intro = "My name is {} and I am from {}"
country = "India"
name = "Himanshi"
# name will go to first bracket and country will go to second bracket
print(Intro.format(name, country))
Intro1 = "My name is {1} and I am from {0}"
country = "India"
name = "Himanshi"
# or give orderwise numbers in bracket then in format we can pass values in that order
print(Intro.format(country, name))

# F-STRING(MORE CONVINIENT WAY)

print(f"My name is {name} and I am from {country}")

# it will only take 4 decimal values of price
price = 56.08888888
txt = f"For only {price:.4f} dollars!"
print(txt)

print(f"{20*3}")  # output will be in form of string
print(type(f"{20*3}"))  # output will be in form of string

# if we don't want to replace the variables and print it as it is
intro2 = f"My name is {{name}} and I am from {{country}}"

print(intro2)
