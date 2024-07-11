# Python Definitions and Examples

# Conditional Statements: Used to perform different actions based on different conditions.
x = 10
if x > 5:
    print("x is greater than 5")  # Output: x is greater than 5
elif x == 5:
    print("x is 5")
else:
    print("x is less than 5")

# Loop: Used to repeat a block of code multiple times.
# For Loop: Iterates over a sequence (like a list) and executes code for each element.
for i in range(3):
    print(i)  # Output: 0, 1, 2

# While Loop: Repeatedly executes code as long as a condition is true.
i = 0
while i < 3:
    print(i)  # Output: 0, 1, 2
    i += 1

# Difference between break, continue, and pass
for i in range(5):
    if i == 2:
        break  # Exits the loop when i is 2
    print(i)  # Output: 0, 1

for i in range(5):
    if i == 2:
        continue  # Skips the rest of the loop when i is 2
    print(i)  # Output: 0, 1, 3, 4

for i in range(5):
    if i == 2:
        pass  # Does nothing
    print(i)  # Output: 0, 1, 2, 3, 4

# Named Arguments: Passed to a function by explicitly specifying the name of the parameter.
def greet(name, message):
    print(f"Hello, {name}! {message}")

greet(name="Alice", message="Welcome!")  # Output: Hello, Alice! Welcome!

# Different Functional Parameters
# Positional Parameters
def add(a, b):
    return a + b

print(add(2, 3))  # Output: 5

# Default Parameters
def add(a, b=3):
    return a + b

print(add(2))  # Output: 5

# Variable-length Positional Parameters (*args)
def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

print(multiply(1, 2, 3))  # Output: 6

# Variable-length Keyword Parameters (**kwargs)
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30)  # Output: name: Alice, age: 30

# Membership Operators: Used to test if a value is present in a sequence.
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # Output: True
print("orange" not in fruits)  # Output: True

# .center() Method: Centers a string within a specified width.
text = "hello"
print(text.center(10))  # Output: '  hello   '
print(text.center(10, '*'))  # Output: '**hello***'

# .capitalize() Method: Capitalizes the first character of a string.
text = "hello world"
print(text.capitalize())  # Output: Hello world

# .title() Method: Capitalizes the first character of each word.
text = "hello world"
print(text.title())  # Output: Hello World

# .endswith() Method: Checks if a string ends with the specified suffix.
filename = "example.txt"
print(filename.endswith(".txt"))  # Output: True

# len() Function: Returns the number of items in an object.
my_list = [1, 2, 3, 4]
print(len(my_list))  # Output: 4

# range() Function: Generates a sequence of numbers.
for i in range(5):
    print(i)  # Output: 0, 1, 2, 3, 4

# Dictionary: Unordered collection of key-value pairs.
my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice
my_dict["city"] = "New York"
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}
del my_dict["age"]
print(my_dict)  # Output: {'name': 'Alice', 'city': 'New York'}

# .append() Method: Adds a single element to the end of a list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]

# .extend() Method: Extends the list by appending all elements from an iterable.
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Sorting a Set: Convert to list and sort.
my_set = {5, 3, 9, 1, 2}
sorted_list = sorted(my_set)
print(sorted_list)  # Output: [1, 2, 3, 5, 9]

# Sorting a List
my_list = [3, 1, 4, 1, 5, 9, 2]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 4, 5, 9]

# Using sorted() function
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)  # Output: [9, 5, 4, 3, 2, 1, 1]

# Tuples: Immutable ordered collection of items.
my_tuple = (1, 2, 3)
print(my_tuple)  # Output: (1, 2, 3)
print(my_tuple[1])  # Output: 2

# Tuple Unpacking
a, b, c = my_tuple
print(a, b, c)  # Output: 1 2 3

# Sets: Unordered collection of unique elements.
my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Adding and Removing Elements in a Set
my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5}

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Union: {1, 2, 3, 4, 5}
print(set1 & set2)  # Intersection: {3}
print(set1 - set2)  # Difference: {1, 2}

# List Comprehensions: Concise way to create lists.
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Output: [0, 4, 16, 36, 64]

# Dictionary Comprehensions: Creating dictionaries.
squares_dict = {x: x**2 for x in range(10)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Lambda Functions: Small anonymous functions.
add = lambda a, b: a + b
print(add(2, 3))  # Output: 5

# Using Lambda with sorted()
my_list = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]

# Map, Filter, and Reduce
# map() Function: Applies a function to all items in an input list.
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# filter() Function: Filters the elements of an input list using a function.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# reduce() Function: Applies a rolling computation to sequential pairs of values in a list.
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Decorators: Modify the behavior of a function or method.
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.

# Generators: Functions that return an iterable set of items, one at a time.
def my_generator():
    for i in range(3):
        yield i

for value in my_generator():
    print(value)  # Output: 0, 1, 2

# Exception Handling: Handle exceptions that occur during program execution.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("This will always execute.")
# Output: Cannot divide by zero.
# This will always execute.

# File Handling: Work with files to read and write data.
# Reading a File
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a File
with open('example.txt', 'w') as file:
    file.write("Hello, world!")

# Classes and Objects: Define classes and create objects.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", 3)
my_dog.bark()  # Output: Buddy says woof!
