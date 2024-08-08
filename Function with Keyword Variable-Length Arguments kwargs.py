# Title: Function with Keyword Variable-Length Arguments (**kwargs)

# Definition of the function that takes variable-length keyword arguments
def myfun(**kwargs):
    # Loop through each key-value pair in kwargs and print it
    for key, val in kwargs.items():
        print(f"{key} === {val}")
    # Print a separator line
    print("===================")

# Call the function with different sets of keyword arguments
myfun(name="shilpa", age="88")
myfun(roll=11, sname="amit", fees=9999)
