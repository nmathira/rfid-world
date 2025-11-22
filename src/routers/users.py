from fastapi import APIRouter, HTTPException
from src.models.users import User

router = APIRouter(prefix="/users", tags=["users"])

# GET /users
@router.get("/")
async def list_users():
    return await User.find_all().to_list()


# GET /users/{id}
@router.get("/{user_id}")
async def get_user(user_id: str):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user


# PATCH /users/{id} - rename
from pydantic import BaseModel

class RenameRequest(BaseModel):
    name: str

@router.patch("/{user_id}")
async def rename_user(user_id: str, req: RenameRequest):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(404, "User not found")

    user.name = req.name
    await user.save()
    return {"status": "ok", "new_name": user.name}
