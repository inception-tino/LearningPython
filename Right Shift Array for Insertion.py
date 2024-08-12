"""
Right shift the array to insert an element
"""

arr = [22, 33, 44, 55, 66]  # Initial array
n = len(arr)  # Length of the array
ind = 2  # Index where the element should be inserted
ele = 999  # Element to be inserted

# Append None to make space for the new element
arr.append(None)  # [22, 33, 44, 55, 66, None]

# Right shift elements to make space at the required index
for i in range(n, ind, -1):
    arr[i] = arr[i-1]  # Shift elements to the right

# Insert the new element at the specified index
arr[ind] = ele  # [22, 33, 999, 44, 55, 66]

print("Updated array:", arr)  # Output the updated array
