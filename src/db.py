import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
        ''')
        self.conn.commit()

    def add_expense(self, date, category, amount, description):
        if date and category and amount and description:
            self.cursor.execute('''
                INSERT INTO expenses (date, category, amount, description)
                VALUES (?, ?, ?, ?)
            ''', (date, category, amount, description))
            self.conn.commit()
        else:
            print("Incomplete expense details. Please provide all fields.")

    def view_expenses(self):
        self.cursor.execute('SELECT * FROM expenses')
        expenses = self.cursor.fetchall()
        if expenses:
            print("Expenses:")
            for expense in expenses:
                print(f"ID: {expense[0]}, Date: {expense[1]}, Category: {expense[2]}, Amount: {expense[3]}, Description: {expense[4]}")
        else:
            print("No expenses found.")

    def close(self):
        self.conn.close()

