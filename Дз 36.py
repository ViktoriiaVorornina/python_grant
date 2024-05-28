import json
class EntityFactory:
    def create_book(self, title, author, isbn):
        return Book(title, author, isbn)

    def create_librarian(self, name, employee_id):
        return Librarian(name, employee_id)

    def create_reader(self, name, library_card_number):
        return Reader(name, library_card_number)

class StorageStrategy:
    def save(self, data, filename):
        raise NotImplementedError()

    def load(self, filename):
        raise NotImplementedError()

class JsonStorage(StorageStrategy):
    def save(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load(self, filename):
        with open(filename, 'r') as file:
            return json.load(file)

class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.log_file = open("log.txt", "a")
        return cls._instance

    def log(self, message):
        self.log_file.write(message + '\n')

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Librarian:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

class Reader:
    def __init__(self, name, library_card_number):
        self.name = name
        self.library_card_number = library_card_number

class BookController:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        Logger().log(f"Book added: {book.title}")

    def remove_book(self, book):
        self.books.remove(book)
        Logger().log(f"Book removed: {book.title}")

    def find_book_by_title(self, title):
        return [book for book in self.books if book.title == title]

    def find_book_by_author(self, author):
        return [book for book in self.books if book.author == author]

class LibrarianController:
    def __init__(self):
        self.librarians = []

    def add_librarian(self, librarian):
        self.librarians.append(librarian)
        Logger().log(f"Librarian added: {librarian.name}")

    def remove_librarian(self, librarian):
        self.librarians.remove(librarian)
        Logger().log(f"Librarian removed: {librarian.name}")

    def find_librarian_by_name(self, name):
        return [librarian for librarian in self.librarians if librarian.name == name]

class ReaderController:
    def __init__(self):
        self.readers = []

    def add_reader(self, reader):
        self.readers.append(reader)
        Logger().log(f"Reader added: {reader.name}")

    def remove_reader(self, reader):
        self.readers.remove(reader)
        Logger().log(f"Reader removed: {reader.name}")

    def find_reader_by_name(self, name):
        return [reader for reader in self.readers if reader.name == name]

entity_factory = EntityFactory()
book_controller = BookController()
book_controller.add_book(entity_factory.create_book("The blood and cender", "F. VVV", "112233"))
librarian_controller = LibrarianController()
librarian_controller.add_librarian(entity_factory.create_librarian("ITStep", "LIB001"))

reader_controller = ReaderController()
reader_controller.add_reader(entity_factory.create_reader("Viktoriia Voronina", "CARD001"))

storage_strategy = JsonStorage()
storage_strategy.save({
    "books": [book.__dict__ for book in book_controller.books],
    "librarians": [librarian.__dict__ for librarian in librarian_controller.librarians],
    "readers": [reader.__dict__ for reader in reader_controller.readers]
}, "data.json")

data = storage_strategy.load("data.json")
