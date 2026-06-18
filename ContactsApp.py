# contacts_app.py
"""
Contacts App — Lists + Dictionaries
=====================================
Key intuition:
  - dict  → one contact card  {"name": "Guddu", "phone": "9876543210"}
  - list  → the whole phonebook  [card1, card2, card3]
  - list of dicts = a table. Each dict is a row. Each key is a column.

Features:
  1. print_all_contacts()  → loop through the list, print each dict's values
  2. search_by_name()      → loop + compare, using .lower() for case safety
  3. add_contact()         → build a new dict, append it to the list
"""

# The phonebook
# 4 preloaded contacts
# Each contact is a dict with exactly two keys: 'name' and 'phone'.

contacts = [
    {"name": "Guddu", "phone": "9876543210"},
    {"name": "Zainn", "phone": "9123456789"},
    {"name": "Reeya", "phone": "9988776655"},
    {"name": "Julie", "phone": "9001122334"},
]
# Function 1: Print all contacts
def print_all_contacts(contacts):
    
    print("\n📒 All Contacts")
    print("-" * 30)

    if not contacts:    #for empty list
        print("  No contacts saved yet.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"  {i}. {contact['name']:<15} {contact['phone']}")

    print("-" * 30)


# Function 2: Search by name
def search_by_name(contacts, search_name):
    
    print(f"\n🔍 Searching for '{search_name}'...")

    found = False

    for contact in contacts:
        if contact["name"].lower() == search_name.lower():
            print(f"  ✅ Found: {contact['name']} → {contact['phone']}")
            found = True

    if not found:
        print(f"  ❌ No contact named '{search_name}'.")


# function 3: search by number
def search_by_number(contacts, search_phone):
   
    print(f"\n🔍 Searching for number '{search_phone}'...")
 
    found = False
 
    for contact in contacts:
        if contact["phone"].strip() == search_phone.strip():
            print(f"  ✅ Found: {contact['name']} → {contact['phone']}")
            found = True
 
    if not found:
        print(f"  ❌ No contact with number '{search_phone}'.")


# Function 4: Add a new contact 
def add_contact(contacts, name, phone):
  
    new_contact = {"name": name, "phone": phone}
    contacts.append(new_contact)
    print(f"\n  ✅ '{name}' added to contacts.")


# Main flow

# Intuition:
#   while True = run forever UNTIL the user chooses to exit.
#   Each iteration: show menu -> take input -> call the right function.
#   'break' is the only exit — it kills the while loop when user picks 5.
#   The 'else' at the bottom catches anything that isn't 1-5.
 
print("=" * 35)
print("        CONTACTS APP")
print("=" * 35)
 
while True:
    print("\nWhat do you want to do?")
    print("  1. Display all contacts")
    print("  2. Search by name")
    print("  3. Search by number")
    print("  4. Add new contact")
    print("  5. Exit")
 
    choice = input("\nEnter choice (1–5): ").strip()
 
    if choice == "1":
        print_all_contacts(contacts)
 
    elif choice == "2":
        name = input("  Enter name to search: ")
        search_by_name(contacts, name)
 
    elif choice == "3":
        phone = input("  Enter number to search: ")
        search_by_number(contacts, phone)
 
    elif choice == "4":
        name  = input("  Enter name: ")
        phone = input("  Enter phone number: ")
        add_contact(contacts, name, phone)
 
    elif choice == "5":
        print("\n  👋 Bye!")
        break
 
    else:
        print("  ⚠️  Invalid choice. Please enter a number between 1 and 5.")