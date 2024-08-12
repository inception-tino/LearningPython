import os

# Step 1: Check if the base directory 'test' exists, if not, create it
if os.path.exists("test") == False:
    os.mkdir("test")

# Step 2: Loop to ask for folder names
while True:
    name = input("Enter the folder name = ")

    # Step 3: Check if the folder already exists in the 'test' directory
    if os.path.exists("test/" + name) == True:
        print("This folder already exists")
    else:
        # Step 4: Create the folder if it doesn't exist
        os.mkdir("test/" + name)

    # Step 5: Ask the user if they want to continue
    cont = int(input("Enter 1 to continue = "))
    if cont != 1:
        break  # Exit the loop if the user doesn't enter 1

