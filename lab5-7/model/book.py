class Book:
    '''Has the following properties:
        -id
        -title
        -description
        -author
    '''

    def __init__(self, id, title, description, author):
        self._id = id
        self._title = title
        self._description = description
        self._author = author

    def __repr__(self):
        #Prints the book's details

        return "Book #%d:\nTitle: %s\nDescription: %s\nAuthor: %s\n" % (self._id, self._title, self._description, self._author)

    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.__dict__ == other.__dict__)

    def getId(self):
        #Returns the id of the book

        return self._id

    def setId(self, id):
        #sets the book's id

        self._id = id

    def getTitle(self):
        #Returns the book's title

        return self._title

    def setTitle(self, title):
        #Sets the book's title

        self._title = title

    def getDescription(self):
        #Returns the book's description

        return self._description

    def setDescription(self, description):
        #Sets the book's description

        self._description = description

    def getAuthor(self):
        #Returns the book's author

        return self._author

    def setAuthor(self, author):
        #Sets the book's author

        self._author = author
