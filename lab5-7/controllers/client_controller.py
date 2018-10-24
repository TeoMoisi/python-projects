import pickle
from repository.book_repo import BookRepository
from repository.loan_repo import LoanRepository
from repository.client_repo import ClientRepository
from model.exception import LibraryException
from model.book import Book

import operator

class ClientController:

    def __init__(self, repo_client):

        self._repo_client = repo_client

    def getLibrary(self):
        #Lists all the books and the clients.

        return self._repo_client.getLibrary()

    def addClient(self, client):
        #Adds a new client.

        self._repo_client.addClient(client)

    def removeClient(self, clientId):
        #Removes a client by its given id.

        for client in [loan.getClient() for loan in self._repo_client.getLoans()]:
            if client.getId() == clientId:
                raise LibraryException("Client has rented book, please return them and then remove him.")
        self._repo_client.removeClient(clientId)

    def updateClientId(self, clientId, newId):
        #Updates a client's id.

        self._repo_client.updateClientId(clientId, newId)

    def updateClientName(self, clientId, nwName):
        #Updates the name of a client.

        self._repo_client.updateClientName(clientId, nwName)

    def getClients(self):
        #ListS all the clients at this moment in the Library
        return self._repo_client.getClients()

    def save(self):
        #Saves the whole information in repo.bin

        self._repo_client.saveHistory()


    def recreate(self):
        #Creates a new library
        self._repo_client.createNew_Lib()