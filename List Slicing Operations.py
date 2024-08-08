# Title: List Slicing Operations

# Initialize a list with some values
l = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# Print different slices of the list
print("l[:] ", l[:])          # Output: [11, 22, 33, 44, 55, 66, 77, 88, 99]
print("l[2:] ", l[2:])        # Output: [33, 44, 55, 66, 77, 88, 99]
print("l[:6] ", l[:6])        # Output: [11, 22, 33, 44, 55, 66]
print("l[1:6:2] ", l[1:6:2])  # Output: [22, 44, 66]
print("l[1::2] ", l[1::2])    # Output: [22, 44, 66, 88]
print("l[::2] ", l[::2])      # Output: [11, 33, 55, 77, 99]
print("l[:6:2] ", l[:6:2])    # Output: [11, 33, 55]
print("l[7:1:-2] ", l[7:1:-2]) # Output: [88, 66, 44]
print("l[::-1] ", l[::-1])    # Output: [99, 88, 77, 66, 55, 44, 33, 22, 11]
