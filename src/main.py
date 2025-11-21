from fastapi import FastAPI
from src.db import init_db
from src.models.users import User

app = FastAPI()

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/users")
async def list_users():
    users = await User.find_all().to_list()
    return users

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    user = await User.get(user_id)  # now user_id matches _id string
    if not user:
        return {"error": "User not found"}
    return user

@app.get("/test_mongo")
async def test_mongo():
    uri = os.environ.get("MONGO_URI")
    client = AsyncIOMotorClient(uri)

    try:
        db = client["admin"]
        coll = db["system.version"]
        versions = await coll.find().to_list(length=10)

        return {
            "connected": True,
            "versions": versions,
            "uri": uri
        }

    except Exception as e:
        return {
            "connected": False,
            "error": str(e),
            "uri": uri
        }