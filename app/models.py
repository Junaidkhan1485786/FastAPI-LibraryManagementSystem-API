from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    id: int
    username: str
    email: str
    mob_number: int
    qualification: str
    seat_number: int

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    published_date: Optional[str]
    description: Optional[str]
class BookBase(BaseModel):
    title: str
    author: str
    published_date: Optional[str]
    description: Optional[str]

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
class BorrowModel(BaseModel):
    id: int
    user_id: int
    book_id: int
    borrow_date: str
    return_date: Optional[str]
