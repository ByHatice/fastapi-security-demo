from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes.resources import router
from app.models import Item
from app.db import items_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    item1 = Item(name="Laptop", price=9999, quantity=5)
    item2 = Item(name="Keyboard", price=499, quantity=20)
    item3 = Item(name="Mouse", price=299, quantity=15)
    
    items_db[item1.id] = item1
    items_db[item2.id] = item2
    items_db[item3.id] = item3
    
    yield
    
    items_db.clear()


app = FastAPI(
    title="Secure API",
    version="1.0.0",
    lifespan=lifespan    
)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(router)