# Initial list
#left shift op
l = [11, 22, 33, 44]

# Step 1: Store the first element in a temporary variable
temp = l[0]

# Step 2: Shift each element one position to the left
for i in range(len(l) - 1):
    l[i] = l[i + 1]

# Step 3: Place the temporary element at the end of the list
l[-1] = temp

# Print the rotated list
print(l)
