import math    #now all the functions of this package can be used using dot

result=math.sqrt(9)
print(result)

# one more way: 
# from math import sqrt,pi  --------- if we want to import just one or specified no. of functions only

# result=sqrt(9)*pi  ----- now no need of using dot

# from math import * ---- this is not recommended approach as it can lead to confusion,complex and difficulty to understand

# AS KEYWORD::::::::::::::::::::::::::

# import math as m ----- then we can write m instead of math
# from math import pi,sqrt as s --------- then we can write s instead of sqrt everywhere 

# dir method  -- shows all the functions and variables of the package
print(dir(math))

#using user defined module/package
from import2 import *

print(__name__)  #it will give import2 and main both
welcome()
print(himanshi)
