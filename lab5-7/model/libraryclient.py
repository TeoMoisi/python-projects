from model.exception import LibraryException
from model.client import Client

class ClientLibrary:
    #This class is described by clients

    def __init__(self):
        self._clients = []


    def __repr__(self):
        return '\n\n'.join(str(client) for client in self._clients)

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

    def deepCopy(self, other):
        #Function to deepCopy another LibraryRepository to this one

        self._clients = [Client(client.getId(), client.getName()) for client in other.getClients()]