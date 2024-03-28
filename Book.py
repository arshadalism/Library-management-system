import random

from db import book_col
from motor.motor_asyncio import AsyncIOMotorDatabase
import asyncio


class Book:
    def __init__(self, name, writer, genre, pages):
        self.name = name
        self.writer = writer
        self.genre = genre
        self.pages = pages

    def show_book_detail(self):
        return f"{{\"book_name\": {self.name}, \"writer\": \"{self.writer}\", \"genre\": \"{self.genre}\", \"pages\": {self.pages}}}"


class Books(Book):
    def __init__(self, name="Maths", writer="RD Sharma",genre="Science",pages=120):
        super().__init__(name, writer, genre, pages)
        self.books_collection = book_col

    async def add_books(self, *books: Book):
        id_number = random.randint(1, 1000)
        data = []
        for book in books:
            book_data = {"_id": id_number, "book_name": book.name, "writer": book.writer, "genre": book.genre,
                         "pages": book.pages, "available": True}
            data.append(book_data)
        await self.books_collection.insert_many(data)
        return f"Books added successfully with _id {id_number}"

    async def check_collections(self):
        cursor = self.books_collection.find()
        book_data = []
        async for doc in cursor:
            book_data.append(doc)
        return book_data


if __name__ == '__main__':
    pass
    # loop = asyncio.get_event_loop()
    # b1 = Books("Maths", "RD Sharma", "Science", 120)
    # loop.run_until_complete(b1.add_books(Book("To Kill a Mockingbird", "Harper Lee", "Fiction", 281),
    #                     Book("1984", "George Orwell", "Science Fiction", 328),
    #                     Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 180),
    #                     Book("Pride and Prejudice", "Jane Austen", "Romance", 432),
    #                     Book("The Catcher in the Rye", "J.D. Salinger", "Coming-of-age", 277), b1
    #              ))
    # loop.run_until_complete(b1.check_collections())
    # b1 = Book("Maths", "RD Sharma", "Science", 120)
    # print(b1.show_book_detail())



