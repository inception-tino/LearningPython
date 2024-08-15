import os  # Import the os module to interact with the operating system

# List all environment variables
env_vars = os.environ  # os.environ is a dictionary containing all environment variables and their values

for key, value in env_vars.items():  # Loop through each key-value pair in the environment variables dictionary
    print(f"{key}: {value}")  # Print the key (environment variable name) and its corresponding value
