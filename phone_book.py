import sqlite3

# Connect to SQLite database (it will create the database if it doesn't exist)
conn = sqlite3.connect('contacts.db')

# Create a cursor object
cur = conn.cursor()

# Create contacts table if it doesn't exist
cur.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL
    )
''')

def show_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Edit Contact")
    print("4. List Contacts")
    print("5. Exit")

def add():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    cur.execute('INSERT INTO contacts (name, phone) VALUES (?, ?)', (name, phone))
    conn.commit()
    print("Contact added successfully.")

def remove():
    contact_id = input("Enter contact ID to remove: ")
    cur.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))
    conn.commit()
    print("Contact removed successfully.")

def edit():
    contact_id = input("Enter contact ID to edit: ")
    new_name = input("Enter new contact name: ")
    new_phone = input("Enter new contact phone number: ")
    cur.execute('UPDATE contacts SET name = ?, phone = ? WHERE id = ?', (new_name, new_phone, contact_id))
    conn.commit()
    print("Contact updated successfully.")

def list_contacts():
    cur.execute('SELECT * FROM contacts')
    rows = cur.fetchall()
    if rows:
        print("\nContacts:")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    else:
        print("No contacts found.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add()
        elif choice == '2':
            remove()
        elif choice == '3':
            edit()
        elif choice == '4':
            list_contacts()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print(f"You selected option {choice}")

if __name__ == "__main__":
    main()

# Close the connection when the program exits
conn.close()
