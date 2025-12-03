from fastapi import APIRouter, HTTPException
from app.models import Item
from app.db import items_db
from app.validation import validate_name, validate_price, validate_quantity


router = APIRouter(prefix="/api/v1", tags=["items"])

@router.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    sanitized_name = validate_name(item.name)
    validate_price(item.price)
    validate_quantity(item.quantity)
    
    if any(existing.id == item.id for existing in items_db):
        raise HTTPException(status_code=400, detail="ID already exists")
    
    item.name = sanitized_name
    items_db[item.id] = item
    return item

@router.get("/items", response_model=list[Item])
def read_items():
    """Get all items"""
    return list(items_db.values())

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    """Get a specific item by ID"""
    if item_id not in items_db:  # ← Dictionary check
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    """Delete an item by ID"""
    if item_id not in items_db:  # ← Dictionary check
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items_db.pop(item_id)  # ← Dictionary pop
    return deleted_item