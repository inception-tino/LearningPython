import os  # Import the os module for interacting with the operating system

# Iterate over all the items in the current directory
for file_name in os.listdir("."):
    # Check if the item is a file (not a directory)
    if os.path.isfile(file_name):
        print(file_name)  # Print the name of the file
