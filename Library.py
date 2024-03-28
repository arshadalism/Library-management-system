import asyncio
from Schema import Book_issue_data
from db import user_col, book_col
import book_receipt_pdf
import datetime


async def issue_book(issue_data: Book_issue_data):
    book = await book_col.find_one({"book_name": issue_data.book_name, "available": True}, {"_id": 0, "writer": 1, "book_name":1})
    print(book)
    if book:
        await book_col.update_one({"book_name": book['book_name']}, {"$set": {"available": False}})
        return {"message": "Book has been issued successfully."}
    else:
        return "book is not available"


async def deposit_book(deposit_data: Book_issue_data):
    count = await book_col.count_documents({"book_name": deposit_data.book_name, "available": False})
    if count > 0:
        await book_col.update_one({"book_name": result["book_name"]}, {"$set": {"available": True}})
        return "Book deposited successfully."
    else:
        return "No book issued."


async def main():
    data = Book_issue_data(student_name="Arshad", enrollment=2100100484, book_name="To Kill a Mockingbird", library_id="eKjJxX{krn")
    result = await issue_book(data)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())



