"""
arr = [1, 2, 3, 4] => [4, 1, 2, 3]
arr = [5, 6, 7, 8] => [8, 5, 6, 7]
arr = [9, 10, 11] => [11, 9, 10]
"""

# Step 1: Ask the user to enter the array elements
arr = [int(x) for x in input("Enter array elements separated by space: ").split()]

# Step 2: Perform a right shift
shifted_arr = arr[-1:] + arr[:-1]

# Step 3: Print the shifted array
print(f"Array after right shift: {shifted_arr}")
