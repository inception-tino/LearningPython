"""
Concatenation of two arrays alternately using logic
"""

a = [1, 3, 5, 7]
b = [2, 4, 6]

n1 = len(a)  # Number of elements in array 'a'
n2 = len(b)  # Number of elements in array 'b'
n = n1 + n2  # Total number of elements in the result

c = [None] * n  # Initialize the result array with None
ind = 0  # Index for tracking elements in 'c'
i = 0  # Loop index

# Alternately add elements from 'a' and 'b' into 'c'
while i < n:
    if ind < n1:
        c[i] = a[ind]  # Add element from 'a'
        i += 1
    if ind < n2:
        c[i] = b[ind]  # Add element from 'b'
        i += 1
    ind += 1  # Move to the next index

print("Resultant list =", c)  # Output the alternately merged array
