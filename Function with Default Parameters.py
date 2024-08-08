# Title: Function with Default Parameters

# Definition of the function with four parameters, two of which have default values
def add(a, b, c=10, d=0):
    # Print the sum of the parameters
    print("Sum = ", a + b + c + d)

# Call the function with different sets of arguments
add(a=11, b=22)
add(a=1, b=2, c=3)
add(a=44, b=55, c=6, d=1)
