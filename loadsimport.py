# Importing the os module, which allows interaction with the operating system
import os

# Change the current working directory to 'test/sample1'
os.chdir("test/sample1")

# Open a file named 'file1.txt' in write mode ('w')
# The 'with' statement ensures that the file is closed automatically after writing
with open("file1.txt", "w") as f:
    # Write the string "Python files" into 'file1.txt'
    f.write("Python files")

# Remove the file 'file1.txt' from the 'test/sample1' directory
os.remove("file1.txt")
