# Title: Using the `remove` Method with Exception Handling

# Initialize a list with some values
l = [11, 22, 33, 44, 55, 66, 22, 77, 22, 99, 100, 111]

# Remove the first occurrence of 22 from the list
l.remove(22)
# Print the list after removing the element
print(l)  # Output: [11, 33, 44, 55, 66, 22, 77, 22, 99, 100, 111]

# Initialize the list again with the same values
l = [11, 22, 33, 44, 55, 66, 22, 77, 22, 99, 100, 111]

# Attempt to remove 222 from the list (will cause an error because 222 is not in the list)
try:
    l.remove(222)
    # Print the list if no error occurs
    print(l)
except ValueError:
    # Print a message if the value does not exist in the list
    print("The value does not exist")
