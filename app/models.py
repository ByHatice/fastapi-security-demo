from pydantic import BaseModel, Field
import uuid 

class itemCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Item name")
    price: float = Field(..., ge=0, le=10000, description="Item price")
    quantity: int = Field(..., ge=0, le=1000, description="Item quantity")

class Item(itemCreate):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))