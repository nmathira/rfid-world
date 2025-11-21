import motor.motor_asyncio
from beanie import init_beanie
from src.models.users import User
import os

from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")
DB_NAME = os.environ.get("MONGO_DB_NAME")

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]

    await init_beanie(
        database=db,
        document_models=[User],
    )
