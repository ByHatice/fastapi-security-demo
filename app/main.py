from fastapi import FastAPI
from app.routes.resources import router

app = FastAPI(title="Secure API", version="1.0.0")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

app.include_router(router)