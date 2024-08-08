# Title: List Slicing Operations with Various Steps

# Initialize a list with some values
l = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# Print different slices of the list
print("l[-5:] ", l[-5:])            # Output: [55, 66, 77, 88, 99]
print("l[7:-1] ", l[7:-1])          # Output: [88]
print("l[-7:-1:2] ", l[-7:-1:2])    # Output: [33, 55, 77]
print("l[-7:2] ", l[-7:2])          # Output: []
print("l[7:2] ", l[7:2])            # Output: []
print("l[2:-2] ", l[2:-2])          # Output: [33, 44, 55, 66, 77]
print("l[6:-5] ", l[6:-5])          # Output: []
print("l[6:-5:-1] ", l[6:-5:-1])    # Output: [77, 66]
