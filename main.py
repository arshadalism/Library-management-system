class Book:
    def __init__(self, name: str, writer:str, genre:str, pages:int):
        self.b_name = name
        self.writer = writer
        self.genre = genre
        self.pages = pages


class Books(Book):
    def __init__(self, name: str = "BOOK!", writer: str = "Arshad", genre: str = "Thriller", pages: int = 100):
        super().__init__(name, writer, genre, pages)  # Call the superclass constructor
        self.library = []

    def add_book(self, book: Book):
        self.library.append({'name': book.b_name, 'writer': book.writer, 'genre': book.genre, 'pages': book.pages})

    def check_out_books(self):
        return self.library


class Student:
    def __init__(self, name: str, enrollment: int, course:str):
        self.name = name
        self.enrollment = enrollment
        self.course = course

    def book_issue(self, books: Books):
        if books.check_out_books():
            return f"Book '{books.check_out_books()[2]['name']}' issued to {self.name}"
        else:
            return "No books available to issue"


if __name__ == '__main__':
    book1 = Book('Book1', 'Author1', 'Genre1', 200)
    book2 = Book('Book2', 'Author2', 'Genre2', 250)
    book3 = Book('MultiDimensional', 'Dr', 'Reasoning', 238)

    books_library = Books()
    books_library.add_book(book1)
    books_library.add_book(book2)
    books_library.add_book(book3)

    # print(books_library.check_out_books())

    stud1 = Student('Arshad', 2100100484, 'B-tech')
    print(stud1.book_issue(books_library))
