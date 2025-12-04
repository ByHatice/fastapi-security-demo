from fastapi import APIRouter, HTTPException
from app.models import Item, itemCreate
from app.db import items_db
from app.validation import validate_name, validate_price, validate_quantity


router = APIRouter(prefix="/api/v1", tags=["items"])

@router.post("/items", response_model=Item, status_code=201)
def create_item(item_create: itemCreate):

    # Validate
    sanitized_name = validate_name(item_create.name)
    validate_price(item_create.price)
    validate_quantity(item_create.quantity)
    
    # Create item
    item = Item(
        name=sanitized_name,
        price=item_create.price,
        quantity=item_create.quantity
    )
    
    # Store
    items_db[item.id] = item
    return item

@router.get("/items", response_model=list[Item])
def read_items():
    """Get all items"""
    return list(items_db.values())

@router.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):  
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_id]

@router.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: str): 
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db.pop(item_id)