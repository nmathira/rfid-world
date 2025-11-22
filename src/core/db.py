from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.core.config import settings

from src.models.users import User

async def init_db():
    client = AsyncIOMotorClient(settings.mongo_uri)
    db = client[settings.mongo_db_name]

    await init_beanie(
        database=db,
        document_models=[
            User,
        ],
    )
