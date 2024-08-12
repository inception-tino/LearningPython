"""
n = 12345 => 54321
n = 9876 => 6789
n = 100 => 001 => 1
n = 456 => 654
"""

# Step 1: Ask the user to enter a number
n = int(input("Enter a number: "))

# Step 2: Convert the number to a string and reverse it
reversed_n = str(n)[::-1]

# Step 3: Convert the reversed string back to an integer
reversed_n = int(reversed_n)

# Step 4: Print the reversed number
print(f"The reversed number is {reversed_n}.")
