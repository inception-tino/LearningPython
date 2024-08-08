# Title: List Operations: Append and Extend

# Initialize an empty list
l = []

# Print the initial empty list
print(l)

# Append individual elements to the list
l.append(11)
l.append(22)
l.append(33)

# Append a list as a single element to the list
l.append([1, 2, 3])

# Extend the list by appending elements from another list
l.extend([10, 20, 30])

# Append a tuple as a single element to the list
l.append((1, 2, 3))

# Extend the list by appending elements from a tuple
l.extend((10, 20, 30))

# Print the final list after all operations
print(l)
