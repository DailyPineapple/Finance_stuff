import typer
from src.db import Database
import datetime as dt

app = typer.Typer()

@app.command()
def create_tables():
    db = Database()
    db.create_tables()
    db.close()
    typer.echo("Tables created successfully.")

@app.command()
def add_expense(
    Date: str = dt.datetime.now(),
    Category: str = typer.Option(..., help="Enter the expense category"),
    Amount: float = typer.Option(..., help="Enter the amount paid in float format (using a dot)"),
    Description: str = typer.Option(..., help="Enter the description of the item")
):
    db = Database("finance_tracker.db")
    db.add_expense(Date, Category, Amount, Description)
    db.close()
    typer.echo("Expense added successfully.")

@app.command()
def view_expenses():
    db = Database("finance_tracker.db")
    db.view_expenses()
    db.close()

if __name__ == "__main__":
    app()
