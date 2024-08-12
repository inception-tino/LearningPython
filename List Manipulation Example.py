l = [44, 55]  # Initial list
n = len(l)  # Get the length of the list, which is 2
l.append(None)  # Extend the list by appending None
# l is now [44, 55, None]

l[2] = l[1]  # Shift the element at index 1 to index 2
# l is now [44, 55, 55]

ele = 66  # Element to be inserted
ind = 1  # Index at which to insert the element

# Insert the element at the specified index
if 0 <= ind <= n:  # Check if the index is valid
    l[ind] = ele  # Insert the element
else:
    print("Invalid index")

print(l)  # Final list
# Output: [44, 66, 55]
