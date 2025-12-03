from app.models import Item

items_db: dict[int, Item] = {}

def add_item(item: Item) -> int:
    if item.id in items_db:
        raise ValueError("Item with this ID already exists.")
    items_db[item.id] = item
    return item.id
