# Get input string from the user
user_input = input("Enter a string: ")

# Split the input string into words
words = user_input.split()

# Check if there are 2 or more words
if len(words) >= 2:
    # Initialize the count for words starting with A, S, or E
    count = 0
    for word in words:
        # Check if the word starts with A, S, or E (case insensitive)
        if word[0].upper() in ['A', 'S', 'E']:
            count += 1
    print(f"Number of words starting with A, S, or E: {count}")
else:
    print("The string must contain at least two words.")
