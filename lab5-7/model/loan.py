class Loan:
    '''This class has the following properites: a client can rent more books at a time, but a book can be rented by only one client at a time.
    It is described by: clientName and bookId.
    '''
    def __init__(self, client, book):
        self._client = client
        self._book = book

    def __repr__(self):

        return "Client %s has the book #%d with the Title: %s" % (self._client.getName(), self._book.getId(), self._book.getTitle())

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def getClient(self):
        return self._client

    def getBook(self):
        return self._book