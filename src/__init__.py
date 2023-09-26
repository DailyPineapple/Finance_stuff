import datetime


class AddItem:
    def __init__(self, item, category,
                 price=None):
        self.item = item
        self.category = category
        self.price = price
        self.date_added = datetime.datetime.now().isoformat()

    def __repr__(self) -> str:
        return f"({self.item}, {self.category}, {self.price}, {self.date_added})"
