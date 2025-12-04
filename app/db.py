from app.models import Item

items_db: dict[str, Item] = {}

def add_item(item: Item) -> str:
    if item.id in items_db:
        raise ValueError("Item with this ID already exists.")
    items_db[item.id] = item
    return item.id