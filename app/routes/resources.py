from fastapi import APIRouter, HTTPException
from app.models import Item
from app.db import items_db
from app.validation import validate_name, validate_price, validate_quantity

router = APIRouter()

@router.post("/items/", response_model=Item)
def create_item(item: Item):
    validate_name(item.name)
    validate_price(item.price)
    validate_quantity(item.quantity)
    
    if any(existing.id == item.id for existing in items_db):
        raise HTTPException(status_code=400, detail="ID already exists")
    
    items_db.append(item)
    return item

@router.get("/items/", response_model=list[Item])
def read_items():
    return items_db

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            deleted_item = items_db.pop(index)
            return deleted_item
    raise HTTPException(status_code=404, detail="Item not found")