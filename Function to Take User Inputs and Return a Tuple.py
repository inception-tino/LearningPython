# Title: Function to Take User Inputs and Return a Tuple

# Definition of the function to take inputs
def takeInputs():
    # Prompt the user to enter a name
    name = input("Enter the name = ")
    # Prompt the user to enter an age
    age = input("Enter the age = ")
    # Prompt the user to enter a gender
    gender = input("Enter the gender = ")
    # Return the entered values as a tuple
    return name, age, gender

# Call the function and store the returned tuple in mydata
mydata = takeInputs()

# Print the returned tuple
print(mydata)

# Prompt the user for another set of inputs
name, age, gender = takeInputs()
print(f"NAME = {name} AGE = {age} GENDER = {gender}")

# Call the function again and print the returned tuple
print(takeInputs())
