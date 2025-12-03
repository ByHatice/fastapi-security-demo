from pydantic import BaseModel, Field

class Item(BaseModel):
    id: int = Field(..., ge=1, description="Unique item ID")
    name: str = Field(..., min_length=2, max_length=100, description="Item name")
    price: float = Field(..., ge=0, le=10000, description="Item price")
    quantity: int = Field(..., ge=0, le=1000, description="Item quantity")