from model.book import Book
from model.client import Client
from model.command import Command

from model.exception import LibraryException
from controllers.LibraryController import LibraryController
from repository.LibraryRepository import LibraryRepository

class Tester:
    #This class implements the tests

    def __init__(self):
        pass

    def testBook(self):
        #Tests the functions which returns and sets the values for books

        book = Book(1, "Alice in Wonderland", "Fantasy", "Lewis Carrol")
        assert book.getId() == 1
        assert book.getTitle() == "Alice in Wonderland"
        assert book.getDescription() == "Fantasy"
        assert book.getAuthor() == "Lewis Carrol"
        book.setAuthor("Teofana")
        assert book.getAuthor() == "Teofana"
        book.setTitle("Maths")
        assert book.getTitle() == "Maths"
        book.setDescription("A brief history")
        assert book.getDescription() == "A brief history"

    def testClient(self):
        #tests the function which returns and set the clien details

        client = Client(78, "Maria")
        assert client.getId() == 78
        assert client.getName() == "Maria"
        client.setId(45)
        assert client.getId() == 45
        client.setName("Marian")
        assert client.getName() == "Marian"



''' def testController(self):
        books = []
        clients = []
        testrepo = LibraryRepository(False)
        controller = LibraryController(testrepo)
        cmd = Command("addbook|Harry Potter|Fantasy|J.K.Rowling")
        controller.addBook(cmd.toAddBook(0))
        books.append(cmd.toAddBook(0))
        cmd = Command("addbook|Jane Ayre|Romance|Charlotte Bronte")
        controller.addBook(cmd.toAddBook(1))
        books.append(cmd.toAddBook(1))
        cmd = Command("addclient|99|Alexandra")
        controller.addClient(cmd.toAddClient())
        clients.append(cmd.toAddClient())
        cmd = Command("addclient|100|Paul")
        controller.addClient(cmd.toAddClient())
        clients.append(cmd.toAddClient())
        assert controller.getBooks() == books
        assert controller.getClients() == clients
        cmd = Command("updatename|99|Alexandrina")
        controller.updateClientName(int(cmd.getArg(1)), cmd.getArg(2))
        clients[0].setName("Alexandrina")
        assert controller.getClients() == clients
        cmd = Command("updateId|99|101")
        controller.updateClientId(int(cmd.getArg(1)), int(cmd.getArg(2)))
        clients[1].setId(101)
        cmd = Command("removeClient|101")
        controller.removeClient(int(cmd.getArg(1)))
        clients = clients[:-1]
        #assert controller.getClients() == clients
        cmd = Command("removeBook|1")
        controller.removeBook(int(cmd.getArg(1)))
        books = books[:-1]
        cmd = Command("updateDescription|0|The best book ever written!")
        controller.updateDescription(int(cmd.getArg(1)), cmd.getArg(2))
        books[0].setDescription("The best book ever written!")
        assert controller.getBooks() == books
        assert controller.getBooks() == [Book(0, "Harry Potter", "The best book ever written!", "J.K.Rowling")]
        #assert controller.getBooks() == [Book(1, "Jane Ayre", "Romance", "Charlotte Bronte")]
        assert controller.getClients() == [Client(100, "Paul")]
        assert controller.getBooks() == [Book(0, "Harry Potter", "The best book ever written!", "J.K.Rowling")]
        assert controller.getClients() == [Client(100, "Paul")]

    def testAll(self):
        #Calls all the test functions

        self.testBook()
        self.testClient()
        self.testController()'''