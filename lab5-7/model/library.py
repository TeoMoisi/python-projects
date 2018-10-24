from model.book import Book
from model.client import Client
from model.loan import Loan
from model.exception import LibraryException


class Library:
    #This class is described by books, clients and loans.

    def __init__(self):
        self._books = []
        self._clients = []
        self._loans = []

    def __repr__(self):
        return '\n\n'.join(str(book) for book in self._books) + "\n\n" + '\n\n'.join(str(client) for client in self._clients) + "\n\n"  + '\n\n'.join(str(loan) for loan in self._loans)

    def addBook(self, book):
        #Adds a new book.

        self._books.append(book)

    def getBooks(self):
        #Returns books list

        return self._books

    def removeBook(self, bookId):
        #Removed a book. Raises error when no book was found.

        for i in range(len(self._books)):
            book = self._books[i]
            if book.getId() == bookId:
                del self._books[i]
                return
        raise LibraryException("Book not found!")

    def removeLoanByBook(self, bookId):
        #Removes a Loan by a book id.

        for i in range(len(self._loans)):
            loan = self._loans[i]
            if loan.getBook().getId() == bookId:
                del self._loans[i]
                return
        raise LibraryException("Book not found")

    def updateTitle(self, bookId, newBookTitle):
        #Updates the title of the book.

        for book in self.getBooks():
            if book.getId() == bookId:
                book.setTitle(newBookTitle)
                return
        raise LibraryException("Book not found!")

    def updateDescription(self, bookId, newBookDescription):
        #Updates the description of a given book.

        for book in self.getBooks():
            if book.getId() == bookId:
                book.setDescription(newBookDescription)
                return
        raise LibraryException("Book not found!")

    def updateAuthor(self, bookId, newBookAuthor):
        #Updates the author of a given book.

        for book in self.getBooks():
            if book.getId() == bookId:
                book.setAuthor(newBookAuthor)
                return
        raise LibraryException("Book not found!")

    def searchBook(self, bookId):
        #Seraches for a book with a given id and returns a unique book. Raises an error if the book was not found.

        """for b in self._books:
            if b.book.getId() == bookId:
                return bw
        raise LibraryException("Book not found!")"""
        for i in range(len(self._books)):
            book = self._books[i]
            if book.getId() == bookId:
                return book
        raise LibraryException("Book not found!")

        #for i in range(len(self._books)):
         #   book = self._books[i]
          #  if book.getId() == bookId:
           #     return book
        #raise LibraryException("Book not found!")


    def getBooksSize(self):
        #Returns the book's list size.

        return len(self._books)

    def addClient(self, client):
        #Adds a new client

        try:
            self.searchClient(client.getId())
            raise ValueError("Client Id already exists!")
        except LibraryException:
            self._clients.append(client)

    def updateClientName(self, clientId, clientNewName):
        #Updates the name of a client.

        for client in self.getClients():
            if client.getId() == clientId:
                client.setName(clientNewName)
                return
        raise LibraryException("Client not found!")

    def updateClientId(self, clientId, clientNewId):
        #Updates the id of a client.
        try:
            self.searchClient(clientNewId)
            raise ValueError("Client Id already exists!")
        except LibraryException:
            for client in self.getClients():
                if client.getId() == clientId:
                    client.setId(clientNewId)
                    return
        raise LibraryException("Client not found!")

    def removeClient(self, clientId):
        #Removes a client by a given id.

        for i in range(len(self._clients)):
            client = self._clients[i]
            if client.getId() == clientId:
                del self._clients[i]
                return
        raise LibraryException("Client not found!")

    def searchClient(self, clientId):
        #Seraches for a client by its id.
        for i in range(len(self._clients)):
            client = self._clients[i]
            if client.getId() == clientId:
                return client
        raise LibraryException("Client not found!")

    def getClients(self):
        #Returns the list of the clients.

        return self._clients

    def getLoans(self):
        #Returns the list of the loans.

        return self._loans

    def deepCopy(self, other):
        #Function to deepCopy another LibraryRepository to this one

        self._books = [Book(book.getId(), book.getTitle(), book.getDescription(), book.getAuthor()) for book in other.getBooks()]
        self._clients = [Client(client.getId(), client.getName()) for client in other.getClients()]
        self._loans = [Loan(self.searchClient(loan.getClient().getId()), self.searchBook(loan.getBook().getId())) for loan in other.getLoans()]

    def rentBook(self, clientId, bookID):
        print("jkjscjk")
        print(len(self._clients))
        print(len(self._books))
        clt = self.searchClient(clientId)
        bk = self.searchBook(bookID)
        if bk in [rental.getBook() for rental in self.getLoans()]:
            raise LibraryException("Book already rented to somebody!")
        self._loans.append(Loan(clt, bk))

    def returnBook(self, clientId, bookID):
        client = self.searchClient(clientId)
        book = self.searchBook(bookID)
        if not book in [loan.getBook() for loan in self.getLoans()]:
            raise LibraryException("Book is not rented, how could you return it? Maybe a donation?")
     