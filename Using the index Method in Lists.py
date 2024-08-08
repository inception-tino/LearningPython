# Title: Using the `index` Method in Lists

# Initialize a list with some values
l = [11, 22, 33, 44, 55, 66, 22, 77, 22, 99, 100, 111]

# Find the index of the first occurrence of 22 in the list
print(l.index(22))  # Output: 1

# Find the index of the first occurrence of 22 in the list starting from index 3
print(l.index(22, 3))  # Output: 6

# Find the index of the first occurrence of 22 in the list between index 7 and 9
print(l.index(22, 7, 9))  # Output: 8
