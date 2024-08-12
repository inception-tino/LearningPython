"""
This program calculates the sum of the first n natural numbers.
For example, if n = 5, the sum will be 1 + 2 + 3 + 4 + 5 = 15.
"""

# Asking the user to give us an n value
n = int(input("Enter n = "))

# Initialize the sum to 0
sum = 0

# Loop from 1 to n (inclusive) to calculate the sum
for i in range(1, n + 1):
    sum += i
    # Print the current step and the sum so far
    print(f"Current i = {i}, Sum = {sum}")

# Finally, print the total sum
print(f"The sum of the first {n} natural numbers is {sum}.")
