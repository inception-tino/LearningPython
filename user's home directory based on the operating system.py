import os  # Import the os module to interact with the operating system

# Determine the home directory based on the operating system
if os.name == 'nt':  # 'nt' indicates that the operating system is Windows
    home_dir = os.environ.get("USERPROFILE")  # Get the home directory path from the 'USERPROFILE' environment variable
else:  # If the operating system is not Windows (e.g., it's Unix-like such as Linux or macOS)
    home_dir = os.environ.get("HOME")  # Get the home directory path from the 'HOME' environment variable

print(f"The home directory is: {home_dir}")  # Print the home directory path
