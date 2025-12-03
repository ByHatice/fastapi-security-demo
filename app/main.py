from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.routes.resources import router
from app.models import Item
from app.db import items_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    items_db[1] = Item(id=1, name="Laptop", price=9999, quantity=5)
    items_db[2] = Item(id=2, name="Keyboard", price=499, quantity=20)
    items_db[3] = Item(id=3, name="Mouse", price=299, quantity=15)
    
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