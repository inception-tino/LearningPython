import os  # Importing the os module, which provides a way to interact with the operating system

print(os.getcwd())  # Prints the current working directory

os.chdir("test")  # Changes the current working directory to the 'test' directory

print(os.getcwd())  # Prints the current working directory after the change

os.chdir("..")  # Changes the current working directory to the parent directory (goes up one level)

print(os.getcwd())  # Prints the current working directory after going up one level

