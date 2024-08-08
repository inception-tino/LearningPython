# Title: Iterating Over a List

# Initialize a list with some values
l = [11, 22, 33, 44, 55, 66]

# Print the length of the list
print(len(l))

# Iterate over the list using the range function and print each element with a tab space
for i in range(len(l)):
    print(l[i], end="\t")
else:
    # Print a new line after the loop completes
    print()

# Iterate over the list using a for-each loop and print each element with a tab space
for x in l:
    print(x, end="\t")
