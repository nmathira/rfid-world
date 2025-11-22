from fastapi import FastAPI
from src.core.db import init_db
from src.routers import users_router

app = FastAPI(title="RFID Backend")

@app.on_event("startup")
async def startup_event():
    await init_db()

# include your routers
app.include_router(users_router)

@app.get("/")
async def root():
    return {"status": "ok"}
