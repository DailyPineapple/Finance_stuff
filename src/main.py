from db import Database

database = Database()
database.create_tables()

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
        database.add_expense(date, category, amount, description)

    elif choice == "2":
        database.view_expenses()

    elif choice == "3":
        break

    else:
        print("Invalid choice. Try again.")

database.close()