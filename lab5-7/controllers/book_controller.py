import pickle
from repository.book_repo import BookRepository
from model.exception import LibraryException
from model.book import Book

import operator

class BookController:

    def __init__(self, repo_book):

        self._repo_book = repo_book

    def addBook(self, book):
        #Adds a new book

        self._repo_book.addBook(book)

    def removeBook(self, bookId):
        #removes a book

        for book in [loan.getBook() for loan in self._repo_book.getLoans()]:
            if book.getId() == bookId:
                raise LibraryException("Book rented...")
        self._repo_book.removeBook(bookId)

    def updateTitle(self, bookId, newTitle):
        #Updates a book's title

        self._repo_book.updateTitle(bookId, newTitle)

    def updateDescription(self, bookId, newDescription):
        #Upadates a book's descriprion.

        self._repo_book.updateDescription(bookId, newDescription)

    def updateAuthor(self, bookId, newAuthor):
        #Updates a book's author.

        self._repo_book.updateAuthor(bookId, newAuthor)

    def getLibrary(self):
        #Lists all the books and the clients.

        return self._repo_book.getLibrary()

    def getBooks(self):
        #Lists all the books at this moment in the Library

        return self._repo_book.getBooks()

    def save(self):
        # Saves the whole information in repo.bin

        self._repo_book.saveHistory()

    def recreate(self):
        # Creates a new library
        self._repo_book.createNew_Lib()
