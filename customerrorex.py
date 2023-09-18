# doubttttttttttttttt
a = input("Enter 'quit' or any value between 5 and 9:\n")

if a == 'quit' and (not a.isdigit() or int(a) < 5 or int(a) > 9):
    raise ValueError("Input should be 'quit' or a value between 5 and 9")
