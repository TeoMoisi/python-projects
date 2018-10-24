import atexit

from tests.tester import Tester
from ui.LibraryApplication import LibraryApplication
from controllers.LibraryController import LibraryController
from repository.book_repo import BookRepository
from repository.client_repo import ClientRepository
from repository.loan_repo import LoanRepository

from model.book import Book
from model.client import Client


if __name__ == '__main__':
    tester = Tester()
    #tester.testAll()

    repo_book = BookRepository()
    repo_client = ClientRepository()
    repo_loan = LoanRepository()
    controller = LibraryController(repo_book, repo_client, repo_loan)
    atexit.register(repo_book.saveHistory)
    atexit.register(repo_client.saveHistory)
    atexit.register(repo_loan.saveHistory)

    app_book = LibraryApplication(controller)
    app_book.run()

    #repo_client = ClientRepository()
    #controller_client = ClientController(repo_client)
    #atexit.register(repo_client.saveHistory)
    #app_client = LibraryApplication(controller_client, controller_book, controller_loan)
    #app_client.run()

    #repo_loan = LoanRepository()
    #controller_loan = LoanController(repo_loan)
    #atexit.register(repo_loan.saveHistory)
    #app_loan = LibraryApplication(controller_loan, controller_book, controller_client)
    #app_loan.run()