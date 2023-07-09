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
