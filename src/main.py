import typer
from src.db import Database

database = Database()
app = typer.Typer()


@app.command()
def show():
    database.view_expenses()


if __name__ == "__main__":
    app()
