from pydantic import BaseModel, EmailStr


class User_signup(BaseModel):
    name: str
    enrollment: int
    course: str
    email: EmailStr
    password: int


class User_login(BaseModel):
    email: EmailStr
    password: int
    library_id: str

