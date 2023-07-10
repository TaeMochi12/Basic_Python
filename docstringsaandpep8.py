# Docstrings are the string literals that appear right after the definition of a function,method,class,or module
# docstrings aren't ignored like comments
# docstrings are written just before/above the body of function for documenting the code

import this  # Zen of Python-an easter egg in python


def square(n):
    '''Takes in a number n,returns the square of n'''
    print(n**2)


square(6)
print(square.__doc__)  # prints the docstring as it is using doc attribute

# PEP 8
# It is a document that provides guidelines and best practice on how to write Python code
# focuse is to improve the readability and consistency of code
# PEP-stands for PYTHON ENHANCEMENT PROPOSAL
