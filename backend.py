from fastapi import FastAPI, HTTPException
from Schema import User_signup, User_login, add_book, Book_issue_data
from User import signup, login, get_library_id
import uvicorn
from Book import Books, Book
from Library import issue_book, deposit_book
from fastapi.responses import FileResponse
from book_receipt_pdf import book_issue_receipt

app = FastAPI(title="Library-Management-System")


@app.get("/")
def root():
    return {"Welcome to the Library-Management-System"}


@app.post("/signup")
async def user_signup(user_signup_data:User_signup):
    response = await signup(user_signup_data)
    return response


@app.post("/login")
async def user_login(user_login_data: User_login):
    response = await login(user_login_data)
    return response


@app.get("/libray_id")
async def library_id(enrollment: int):
    response = await get_library_id(enrollment)
    return response


@app.get("/book_collections")
async def book_collection():
    b1 = Books()
    res = await b1.check_collections()
    return res


@app.post("/add_books")
async def add_books(add_book_data: add_book):
    b1 = Books()
    response = await b1.add_books(Book(add_book_data.book_name, add_book_data.writer, add_book_data.genre, add_book_data.pages))
    return response


@app.post("/book_issue")
async def book_issue(student_data: Book_issue_data):
    response = await issue_book(student_data)
    if "message" in response and response["message"] == "Book has been issued successfully.":
        receipt_file = await book_issue_receipt(student_data.student_name, student_data.enrollment, student_data.book_name, student_data.writer)
        return receipt_file
    else:
        return response


if __name__ == '__main__':
    uvicorn.run("backend:app", reload=True)
