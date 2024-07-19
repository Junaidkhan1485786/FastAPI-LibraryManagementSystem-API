from fastapi import APIRouter, HTTPException
from app.crud import create_user, get_user
from app.models import UserModel

router = APIRouter()

@router.post("/", response_model=UserModel)
async def create_new_user(user: UserModel):
    db_user = await get_user(user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return await create_user(user)

@router.get("/{userDetail}", response_model=UserModel)
async def read_user(seat_number: int):
    user = await get_user(seat_number)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

