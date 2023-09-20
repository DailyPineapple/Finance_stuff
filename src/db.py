import sqlite3


class Database:
    def __init__(self) -> None:
        self._connection = sqlite3.connect('finance_tracker.db')

    def close(self) -> None:
        self._connection.close()

    def create_tables(self) -> None:
        """We'll replace this in the future, one step at a time."""
        self._connection.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT)
            """
        )

    def view_expenses(self) -> None:
        cursor = self._connection.execute('SELECT * FROM expenses')
        for row in cursor:
            print(f'ID: {row[0]}')
            print(f'Date: {row[1]}')
            print(f'Category: {row[2]}')
            print(f'Amount: {row[3]}')
            print(f'Description: {row[4]}')
            print('')

    def add_expense(
            self,
            date: str,
            category: str,
            amount: float,
            description: str
    ) -> None:
        self._connection.execute(
            'INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)',
            (date, category, amount, description)
        )
        self._connection.commit()
        print('Expense added successfully')