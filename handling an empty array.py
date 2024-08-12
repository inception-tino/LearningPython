# Step 1: Initialize an empty array
arr = []

# Step 2: Check the length of the array
n = len(arr)

# Step 3: Handle the case when the array is empty
if n == 0:
    print("The array is currently empty.")
    ind = int(input("Enter the index to insert the element (0 for an empty array): "))

    # Step 4: Validate the index input
    if ind != 0:
        print("Invalid index for an empty array. The only valid index is 0.")
    else:
        # Step 5: Get the element to insert
        ele = int(input("Enter the element to insert at index 0: "))
        arr.append(ele)  # Insert the element into the array
        print("Updated array:", arr)
else:
    print("The array is not empty.")
    # You can handle other cases here if the array is not empty
