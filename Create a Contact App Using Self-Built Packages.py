"""
# Basic operations:
1. Add Contact
2. Display Contacts
3. Exit
"""

# Step 1: Define the Contact class
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

# Step 2: Define the ContactBook class
class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)

    def display_contacts(self):
        for contact in self.contacts:
            print(contact)

# Step 3: Main function to manage the app
def main():
    contact_book = ContactBook()
    while True:
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == 2:
            contact_book.display_contacts()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

# Step 4: Run the main function
if __name__ == "__main__":
    main()
