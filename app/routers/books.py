from fastapi import APIRouter, HTTPException, Query, Path
from typing import List
from app.models import Book, BookCreate, BookUpdate
from app.crud import create_book, get_books, get_book, update_book, delete_book

router = APIRouter()

@router.post("/{title}", response_model=Book)
async def create_new_book(book: BookCreate, title: str = Path(..., description="Title of the book to create")):
    new_book = Book(**book.dict(), title=title)
    return await create_book(new_book)


@router.get("/", response_model=List[Book])
async def read_books(title: str = Query(None, description="Filter books by title")):
    if title:
        return [book for book in await get_books() if book.title == title]
    else:
        return await get_books()




@router.get("/{book_id}", response_model=Book)
async def read_book(book_id: str = Path(..., description="ID of the book to retrieve")):
    book = await get_book(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.put("/{book_id}", response_model=Book)
async def update_existing_book(book_id: str, book: BookUpdate):
    updated_book = await update_book(book_id, book)
    if updated_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_book

@router.delete("/{book_id}", response_model=dict)
async def delete_existing_book(book_id: str):
    deleted = await delete_book(book_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}
