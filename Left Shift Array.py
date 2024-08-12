"""
arr = [1, 2, 3, 4] => [2, 3, 4, 1]
arr = [5, 6, 7, 8] => [6, 7, 8, 5]
arr = [9, 10, 11] => [10, 11, 9]
"""

# Step 1: Ask the user to enter the array elements
arr = [int(x) for x in input("Enter array elements separated by space: ").split()]

# Step 2: Perform a left shift
shifted_arr = arr[1:] + arr[:1]

# Step 3: Print the shifted array
print(f"Array after left shift: {shifted_arr}")
