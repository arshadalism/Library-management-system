from pydantic import BaseModel, EmailStr


class User_signup(BaseModel):
    name: str
    enrollment: int
    course: str
    email: EmailStr
    password: str


class User_login(BaseModel):
    email: EmailStr
    password: str
    library_id: str


class Book_issue_data(BaseModel):
    student_name: str
    enrollment: int
    book_name: str
    library_id: str
    writer: str


class add_book(BaseModel):
    book_name: str
    writer: str
    genre: str
    pages: int

