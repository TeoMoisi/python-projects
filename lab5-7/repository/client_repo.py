import pickle

from model.exception import LibraryException
from model.library import Library

class ClientRepository:
    #Contains all the old and new states of the lib_repo

    def __init__(self, restore = True):
        #If there is a saved repo, it is restored, otherwise, it starts with an empty lib

        if restore:
            self.restoreHistory()
        else:
            self.createNew_Lib()

    def get_present(self):
        #Returns the now index

        return self._now

    def getLibrary(self):
        #Returns the actual state of the application
        return self._states[self.get_present()]

    def getCloneStaus(self):
        #Creates a new lib_repo with the same values as the latest one.
        newState = Library()
        newState.deepCopy(self.getLibrary())
        return newState

    def addClient(self, client):
        #Adds a client

        newState = self.getCloneStaus()
        newState.addClient(client)
        self.createNewRepo(newState)

    def getClients(self):
        # lists all the clients at the moment in the lib
        return self.getLibrary().getClients()

    def removeClient(self, clientId):
        #Revmoves a client by its given id.

        newState = self.getCloneStaus()
        newState.removeClient(clientId)
        self.createNewRepo(newState)

    def updateClientId(self, clientId, newId):
        #updates the id of a client
        newState = self.getCloneStaus()
        newState.updateClientId(clientId, newId)
        self.createNewRepo(newState)

    def updateClientName(self, clientId, newName):
        #Updates the anme of a client

        newState = self.getCloneStaus()
        newState.updateClientName(clientId, newName)
        self.createNewRepo(newState)

    def createNewRepo(self, newRepo):
        #Creates a new repo based on the old one
        self.forgetFuture()
        self.createFuture(newRepo)

    def forgetFuture(self):

        self._states = self._states[:self.get_present() + 1]

    def createFuture(self, newRepo):
        #Appends the new repo
        self._states.append(newRepo)
        self._now += 1


    def restoreHistory(self):
        #Stores the most recent histroty_lib trace, pickled in the repo.bin file.
        #If there is no history file, it will return an empty file.
        try:
            with open("repository/repo_client.bin", "rb") as p:
                lastState = pickle.load(p)
                self._states = lastState._states
                self._now = lastState._now
        except IOError:
            self.createNew_Lib()

    def saveHistory(self):
        #Saves the whole app info in repo.bin
        try:
            with open("repository/repo_client.bin", "wb") as p:
                pickle.dump(self, p)
            return "Successfully saved current state!"
        except IOError:
            raise LibraryException("Could not save the current state!")

    def createNew_Lib(self):
        #Creates a new library

        self._states =  [Library()]
        self._now = 0