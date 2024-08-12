"""
Concatenation of two arrays using logic
"""

a = [11, 22, 33, 44]
b = [10, 20, 30]

n1 = len(a)  # Number of elements in array 'a'
n2 = len(b)  # Number of elements in array 'b'
n = n1 + n2  # Total number of elements in the result

c = [None] * n  # Initialize the result array with None

# Filling the result array 'c' with elements from 'a' and 'b'
for i in range(n):
    if i < n1:
        c[i] = a[i]  # Copy elements from 'a' into 'c'
    else:
        c[i] = b[i - n1]  # Copy elements from 'b' into 'c'

print(c)  # Output the concatenated array
