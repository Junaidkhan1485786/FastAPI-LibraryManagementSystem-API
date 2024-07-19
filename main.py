# run app >>>>  python -m uvicorn main:app --reload
from fastapi import FastAPI, Request
from app.routers import users, books, borrows  # Adjusted import path

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(borrows.router, prefix="/borrows", tags=["borrows"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Library Management System API"}
