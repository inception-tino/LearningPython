import os

# C: Create a directory
os.mkdir("foldernew")
print("Directory 'foldernew' created.")

# R: Read/Check if the directory exists
if os.path.exists("foldernew"):
    print("Directory 'foldernew' exists.")
else:
    print("Directory 'foldernew' does not exist.")

# U: Update/Modify - Create a nested directory
os.mkdir("foldernew/myfolder")
print("Nested directory 'foldernew/myfolder' created.")

# D: Delete the nested directory and then the main directory
os.rmdir("foldernew/myfolder")
print("Nested directory 'foldernew/myfolder' deleted.")
os.rmdir("foldernew")
print("Directory 'foldernew' deleted.")
