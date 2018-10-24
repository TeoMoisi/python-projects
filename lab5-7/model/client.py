class Client:
    #A client is described by its name and an id.

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def __repr__(self):
        #Prints the client's details

        return "Client Name: %s with Id: %s" % (self._name, self._id)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def getId(self):
        #Returns the client's id.

        return self._id

    def setId(self, id):
        #Sets the client's id.

        self._id = id

    def getName(self):
        #Returns the client's name.

        return self._name

    def setName(self, name):
        #Sets the client's name.

        self._name = name