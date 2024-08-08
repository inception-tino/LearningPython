# Title: Using the `sorted` Function in Lists

# Initialize a list with some values
l = [4, 99, 6, 22, 77, 22, 99, 100, 111]

# Sort the list in ascending order using the sorted function
a = sorted(l)
# Print the sorted list
print(a)  # Output: [4, 6, 22, 22, 77, 99, 99, 100, 111]

# Print the original list to show it has not been modified
print(l)  # Output: [4, 99, 6, 22, 77, 22, 99, 100, 111]

# Sort the list in descending order using the sorted function
b = sorted(l, reverse=True)
# Print the sorted list in descending order
print(b)  # Output: [111, 100, 99, 99, 77, 22, 22, 6, 4]
