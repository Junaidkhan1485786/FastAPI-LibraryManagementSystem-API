from fastapi import APIRouter, HTTPException
from app.crud import borrow_book, return_book, get_borrow_history
from app.models import BorrowModel

router = APIRouter()

@router.post("/", response_model=BorrowModel)
async def borrow_a_book(borrow: BorrowModel):
    return await borrow_book(borrow)

@router.put("/{borrow_id}", response_model=BorrowModel)
async def return_a_book(borrow_id: str):
    borrow = await return_book(borrow_id)
    if borrow is None:
        raise HTTPException(status_code=404, detail="Borrow entry not found")
    return borrow

@router.get("/{user_id}", response_model=list[BorrowModel])
async def read_borrow_history(user_id: str):
    return await get_borrow_history(user_id)
