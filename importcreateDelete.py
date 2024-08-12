import os  # Import the 'os' module, which provides functions to interact with the operating system.
import shutil  # Import the 'shutil' module, which provides higher-level file operations, like deleting a directory and its contents.

# Step 1: Check if the base directory 'test' exists. If not, create it.
# The 'os.path.exists()' function checks if a file or directory exists at the given path.
# 'os.mkdir()' creates a new directory with the specified name.
if not os.path.exists("test"):
    os.mkdir("test")
    print("Directory 'test' created.")
else:
    print("Directory 'test' already exists.")

# Step 2: Main loop to ask for folder names or delete directories
# A 'while True' loop is an infinite loop that will keep running until explicitly broken.
while True:
    # Prompt the user to either create a new folder or delete an existing directory.
    action = input("Enter 'create' to create a folder or 'delete' to delete a directory: ").strip().lower()

    if action == 'create':
        # This block handles creating a new folder.
        name = input("Enter the folder name: ")  # Ask the user to input the name of the folder they want to create.
        folder_path = "test/" + name  # Construct the full path where the new folder will be created.

        # Check if the folder already exists using 'os.path.exists()'.
        if os.path.exists(folder_path):
            print(f"The folder '{name}' already exists in the 'test' directory.")
        else:
            os.mkdir(folder_path)  # Create the folder using 'os.mkdir()'.
            print(f"Folder '{name}' created successfully inside 'test' directory.")

    elif action == 'delete':
        # This block handles deleting an existing directory.
        dir_name = input(
            "Enter the directory name to delete: ")  # Ask the user for the name of the directory they want to delete.
        dir_path = "test/" + dir_name  # Construct the full path of the directory to be deleted.

        # Check if the directory exists using 'os.path.exists()' and if it's a directory using 'os.path.isdir()'.
        if os.path.exists(dir_path):
            if os.path.isdir(dir_path):
                # Use 'shutil.rmtree()' to remove the directory and all its contents.
                shutil.rmtree(dir_path)
                print(f"Directory '{dir_name}' and all its contents have been deleted.")
            else:
                print(f"'{dir_name}' is not a directory. Deletion aborted.")
        else:
            print(f"Directory '{dir_name}' does not exist in the 'test' directory.")

    else:
        # This block handles invalid actions, i.e., if the user doesn't input 'create' or 'delete'.
        print("Invalid action. Please enter 'create' to create a folder or 'delete' to delete a directory.")

    # Step 5: Ask the user if they want to continue.
    # The script asks the user if they want to continue after performing the create or delete action.
    cont = int(input("Enter 1 to continue or any other key to exit: "))
    if cont != 1:
        break  # The loop breaks, and the script ends if the user enters anything other than 1.

