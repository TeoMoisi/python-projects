import pickle
from repository.book_repo import BookRepository
from repository.loan_repo import LoanRepository
from repository.client_repo import ClientRepository
from model.exception import LibraryException
from model.book import Book

import operator

class LibraryController:

    def __init__(self, repo_book, repo_client, repo_loan):

        self._repo_book = repo_book
        self._repo_client = repo_client
        self._repo_loan = repo_loan

    def addBook(self, book):
        #Adds a new book

        self._repo_book.addBook(book)
        

    def removeBook(self, bookId):
        #removes a book

        for book in [loan.getBook() for loan in self._repo_loan.getLoans()]:
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


    def addClient(self, client):
        #Adds a new client.

        self._repo_client.addClient(client)

    def removeClient(self, clientId):
        #Removes a client by its given id.

        for client in [loan.getClient() for loan in self._repo_loan.getLoans()]:
            if client.getId() == clientId:
                raise LibraryException("Client has rented book, please return them and then remove him.")
        self._repo_book.removeClient(clientId)

    def updateClientId(self, clientId, newId):
        #Updates a client's id.

        self._repo_client.updateClientId(clientId, newId)

    def updateClientName(self, clientId, nwName):
        #Updates the name of a client.

        self._repo_client.updateClientName(clientId, nwName)

    def getLibrary(self):
        #Lists all the books and the clients.

        return self._repo_book.getLibrary()

    def getBooks(self):
        #Lists all the books at this moment in the Library

        return self._repo_book.getBooks()

    def getClients(self):
        #ListS all the clients at this moment in the Library
        return self._repo_client.getClients()

    def getLoans(self):
        #Lists all the loans.

        return self._repo_loan.getLoans()

    def rentBook(self, clientId, bookID):
        #Implements the rent_book function.

        return self._repo_loan.rentBook(clientId, bookID)

    def returnBook(self, clientId, bookID):
        #Implements the return_book function.

        return self._repo_loan.returnBook(clientId, bookID)


    def save(self):
        #Saves the whole information in repo.bin

        self._repo_book.saveHistory()
        self._repo_client.saveHistory()
        self._repo_loan.saveHistory()


    def recreate(self):
        #Creates a new library
        self._repo_book.createNew_Lib()
        self._repo_client.createNew_Lib()
        self._repo_loan.createNew_Lib()

a=BookRepository()
b=ClientRepository()
c=LoanRepository()
x=LibraryController(a,b,c)
book=Book(1,"dsa","asdas","mircea")
x.addBook(book)
print(x.getBooks())