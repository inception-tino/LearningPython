import os  # Imports the os module which provides functions for interacting with the operating system

# Join two paths
path1 = r"C:\Users\natur\PycharmProjects\pythonProject"  # First part of the file path
path2 = "filetext"  # Second part of the file path (the folder or file name within the directory)

# Join path1 and path2 to create a full path
full_path = os.path.join(path1, path2).replace("\\", "/")  # Combines path1 and path2, and replaces backslashes with forward slashes

# Print the full path
print(f"The full path is: {full_path}")  # Prints the complete path formed by joining path1 and path2

# Get the basename of a file
file_path = r"C:\Users\natur\PycharmProjects\pythonProject\filetext"  # Complete file path

# Extracts the basename (the last part of the path, usually the file name)
basename = os.path.basename(file_path)  # Extracts the final component of the file path (e.g., 'filetext')

# Print the basename
print(f"The basename of the file is: {basename}")  # Prints the basename of the path

