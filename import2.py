def welcome():
    print("Hiee!")

himanshi="A beautiful girl"
# to aviod this call when this module is imported we use __name__=="__main__ idiom"

# this idiom determines whether the script is being run directly or being imported as a module into another script

# __name__ tells ki kaha se run ho rha h
print(__name__)

if __name__=="__main__":
    welcome()