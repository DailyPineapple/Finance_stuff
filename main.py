import typer
from src.db import Database as database
import datetime as dt

app = typer.Typer()

@app.command()
def create_tables():
    db = database()
    db.create_tables()
    db.close()
    typer.echo("Tables created successfully.")

@app.command()
def add_expense(
    date_added: str = dt.datetime.today(),
    category: str = typer.Option(..., help="Enter the expense category"),
    amount: float = typer.Option(..., help="Enter the amount paid in float format (using a dot)"),
    description: str = typer.Option(..., help="Enter the description of the item")
):
    db = database("finance_tracker.db")
    db.add_expense(date_added, category, amount, description)
    db.close()
    typer.echo("Expense added successfully.")

@app.command()
def view_expenses():
    db = database("finance_tracker.db")
    db.view_expenses()
    db.close()

if __name__ == "__main__":
    app()
