"""
arr = [1, 2, 3, 4], num = 99, pos = 2 => [1, 99, 2, 3, 4]
arr = [10, 20, 30], num = 25, pos = 1 => [10, 25, 20, 30]
arr = [7, 8], num = 6, pos = 0 => [6, 7, 8]
"""

# Step 1: Ask the user to enter the array elements
arr = [int(x) for x in input("Enter array elements separated by space: ").split()]

# Step 2: Ask the user to enter the number to insert and the position
num = int(input("Enter the number to insert: "))
pos = int(input("Enter the position to insert the number at: "))

# Step 3: Insert the number at the specified position
arr.insert(pos, num)

# Step 4: Print the updated array
print(f"Array after insertion: {arr}")
