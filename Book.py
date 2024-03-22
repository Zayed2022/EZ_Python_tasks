class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_author(self, author):
        self.author = author

    def get_author(self):
        return self.author

    def set_isbn(self, isbn):
        self.isbn = isbn

    def get_isbn(self):
        return self.isbn

def retrieve_books(book_list):
    for book in book_list:
        print("Title:", book.get_title())
        print("Author:", book.get_author())
        print("ISBN:", book.get_isbn())
        print()
if __name__ == "__main__":
    book1 = Book("Wings of Fire", "Abdul Kalam", "9780141036144")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780061120084")
    book_collection = [book1, book2]
    retrieve_books(book_collection)
