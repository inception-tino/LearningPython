# Title: Function with Variable-Length Arguments (*args)

# Definition of the function that takes variable-length arguments
def myfun(*args):
    # Loop through each argument in args and print it
    for x in args:
        print(x)
    # Print a separator line
    print("------------------")

# Call the function with different numbers of arguments
myfun(11, 22, 33)
myfun("shilpa", "python")
myfun(1, 2, 3, 4, 5, 6, 7)
