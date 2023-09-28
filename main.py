import typer
from src.db import Database

app = typer.Typer()

@app.command()
def create_tables():
    db = Database()
    db.create_tables()
    db.close()
    typer.echo("Tables created successfully.")

@app.command()
def add_expense(
    expense_info: str = typer.Option(..., help="Enter the expense details in the format: Date,Category,Amount,Description"),
):
    parts = expense_info.split(',')
    if len(parts) != 4:
        typer.echo("Invalid input format. Please provide Date, Category, Amount, and Description separated by commas.")
        return

    date, category, amount, description = [part.strip() for part in parts]
        
    try:
        amount = float(amount)
    except ValueError:
        typer.echo("Invalid amount format. Amount should be a number.")
        return

    db = Database("finance_tracker.db")
    db.add_expense(date, category, amount, description)
    db.close()
    typer.echo("Expense added successfully.")

@app.command()
def view_expenses():
    db = Database()
    db.view_expenses()
    db.close()

if __name__ == "__main__":
    app()
