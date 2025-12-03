import re
from fastapi import HTTPException

def sanitize_input(text: str) -> str:
    # Remove HTML tags
    text = re.sub(r'<[^>]*>', '', text)
    # Remove script tags
    text = re.sub(r'<script.*?</script>', '', text, flags=re.IGNORECASE | re.DOTALL)
    return text.strip()

def validate_name(name: str) -> str:

    # Sanitize input
    name = sanitize_input(name)

    # Validate
    if not name or name.strip() == "":
        raise HTTPException(status_code=400, detail="Name cannot be empty")
    if not re.match(r"^[a-zA-Z0-9 \-]+$", name):
        raise HTTPException(status_code=400, detail="Only letters, numbers, spaces, and hyphens allowed")
    if len(name) > 100:
        raise HTTPException(status_code=400, detail="Name cannot exceed 100 characters")
    if len(name) < 2:
        raise HTTPException(status_code=400, detail="Name must be at least 2 characters long")

    # Return sanitized name
    return name
    
def validate_price(price: float) -> float:
    if price < 0:
        raise HTTPException(status_code=400, detail="Price cannot be negative")
    if price > 10000:
        raise HTTPException(status_code=400, detail="Price cannot exceed 10,000")
    if not isinstance(price, (int, float)):
        raise HTTPException(status_code=400, detail="Price must be a number")
    
    return price

def validate_quantity(quantity: int):
    if quantity < 0:
        raise HTTPException(status_code=400, detail="Quantity cannot be negative")
    if quantity > 1000:
        raise HTTPException(status_code=400, detail="Quantity cannot exceed 1,000")
    if not isinstance(quantity, int):
        raise HTTPException(status_code=400, detail="Quantity must be an integer")