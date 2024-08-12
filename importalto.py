# Importing the os module for file and directory operations
import os

# Change the current working directory to 'test/sample1'
os.chdir("test/sample1")

# Open a file named 'file1.txt' in write mode
with open("file1.txt", "w") as f:
    # Write the string "Python files" into the file
    f.write("Python files")

# This line is commented out, but it would remove the file 'file1.txt' if uncommented
# os.remove("file1.txt")
