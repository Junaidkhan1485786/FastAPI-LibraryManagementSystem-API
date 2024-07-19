from app.models import UserModel, BookModel, BorrowModel

# In-memory storage
users_db = []
books_db = []
borrows_db = []

async def create_user(user: UserModel):
    users_db.append(user)
    return user

async def get_user(seat_number: int):
    for user in users_db:
        if user.seat_number == seat_number:
            return user
    return None

async def create_book(book: BookModel):
    books_db.append(book)
    return book

async def get_books():
    return books_db

async def get_book(book_id: str):
    for book in books_db:
        if book.title == book_id:
            return book
    return None

async def update_book(book_id: str, book: BookModel):
    for i, b in enumerate(books_db):
        if b.title == book_id:
            books_db[i] = book
            return book
    return None

async def delete_book(book_id: str):
    for i, b in enumerate(books_db):
        if b.title == book_id:
            del books_db[i]
            return True
    return False

async def borrow_book(borrow: BorrowModel):
    borrows_db.append(borrow)
    return borrow

async def return_book(borrow_id: str):
    for borrow in borrows_db:
        if borrow.book_id == borrow_id:
            borrow.return_date = "Returned"
            return borrow
    return None

async def get_borrow_history(user_id: str):
    user_borrows = []
    for borrow in borrows_db:
        if borrow.user_id == user_id:
            user_borrows.append(borrow)
    return user_borrows
