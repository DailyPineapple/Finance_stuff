import sqlite3

# Create a database connection
conn = sqlite3.connect('finance_tracker.db')

# Create a table to store expenses
conn.execute('''CREATE TABLE IF NOT EXISTS expenses
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              date TEXT,
              category TEXT,
              amount REAL,
              description TEXT)''')


# Function to add a new expense to the database
def add_expense(date, category, amount, description):
    conn.execute('''INSERT INTO expenses (date, category, amount, description)
                 VALUES (?, ?, ?, ?)''', (date, category, amount, description))
    conn.commit()
    print("Expense added successfully")


# Function to view all expenses in the database
def view_expenses():
    cursor = conn.execute("SELECT * FROM expenses")
    for row in cursor:
        print(f"ID: {row[0]}")
        print(f"Date: {row[1]}")
        print(f"Category: {row[2]}")
        print(f"Amount: {row[3]}")
        print(f"Description: {row[4]}")
        print("")


# Main program loop
while True:
    print("Enter 1 to add a new expense")
    print("Enter 2 to view all expenses")
    print("Enter 3 to exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        category = input("Enter the category of the expense: ")
        amount = float(input("Enter the amount of the expense: "))
        description = input("Enter a description of the expense: ")
        add_expense(date, category, amount, description)

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        break

    else:
        print("Invalid choice. Try again.")

# Close the database connection
conn.close()