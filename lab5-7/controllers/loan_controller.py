import pickle
from repository.book_repo import BookRepository
from repository.loan_repo import LoanRepository
from repository.client_repo import ClientRepository
from model.exception import LibraryException
from model.book import Book

import operator

class LoanController:

    def __init__(self, repo_loan):

        self._repo_loan = repo_loan

    def getLoans(self):
        #Lists all the loans.

        return self._repo_loan.getLoans()

    def addClient(self, client):
        #Adds a new client.

        self._repo_loan.addClient(client)

    """def getClients(self):
        #ListS all the clients at this moment in the Library
        return self._repo_loan.getClients()"""

    def rentBook(self, clientId, bookID):
        #Implements the rent_book function.

        return self._repo_loan.rentBook(clientId, bookID)

    def returnBook(self, clientId, bookID):
        #Implements the return_book function.

        return self._repo_loan.returnBook(clientId, bookID)


    def save(self):
        #Saves the whole information in repo.bin

        self._repo_loan.saveHistory()


    def recreate(self):
        #Creates a new library
        self._repo_loan.createNew_Lib()