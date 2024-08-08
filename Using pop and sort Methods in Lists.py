# Title: Using `pop` and `sort` Methods in Lists

# Initialize a list with some values
l = [11, 22, 33, 44, 55, 66, 22, 77, 22, 99, 100, 111]

# Pop the last element from the list and store it in x
x = l.pop()
# Print the popped element
print(x)  # Output: 111
# Print the list after popping the last element
print(l)  # Output: [11, 22, 33, 44, 55, 66, 22, 77, 22, 99, 100]

# Pop the element at index 5 from the list
print(l.pop(5))  # Output: 66
# Print the list after popping the element at index 5
print(l)  # Output: [11, 22, 33, 44, 55, 22, 77, 22, 99, 100]

# Initialize the list again with the same values
l = [11, 22, 33, 44, 55, 66, 22, 77, 22, 99, 100, 111]

# Sort the list in ascending order
l.sort()
# Print the sorted list
print(l)  # Output: [11, 22, 22, 22, 33, 44, 55, 66, 77, 99, 100, 111]

# Sort the list in descending order
l.sort(reverse=True)
# Print the sorted list in descending order
print(l)  # Output: [111, 100, 99, 77, 66, 55, 44, 33, 22, 22, 22, 11]
