"""
s = "madam" => palindrome
s = "hello" => not a palindrome
s = "racecar" => palindrome
s = "python" => not a palindrome
"""

# Step 1: Ask the user to enter a string
s = input("Enter a string: ")

# Step 2: Reverse the string
reversed_s = s[::-1]

# Step 3: Compare the original string with the reversed string
if s == reversed_s:
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.")
