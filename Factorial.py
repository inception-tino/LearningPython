"""
n=1 => 1! = 1
n=2 => 2! = 2 * 1 = 2
n=3 => 3! = 3 * 2 * 1 = 6
n=4 => 4! = 4 * 3 * 2 * 1 = 24
n=5 => 5! = 5 * 4 * 3 * 2 * 1 = 120
"""

# Step 1: Ask the user to enter the value of n
n = int(input("Enter the value of n: "))

# Step 2: Initialize the factorial result to 1
factorial = 1

# Step 3: Use a loop to calculate the factorial
for i in range(1, n + 1):
    factorial *= i  # Multiply the current number with the running product
    print(f"Multiplying by {i}, Current Factorial = {factorial}")

# Step 4: Print the final factorial value
print(f"The factorial of {n} is {factorial}.")
