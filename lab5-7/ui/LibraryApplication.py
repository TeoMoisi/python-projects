from model.command import Command
from model.exception import LibraryException
from controllers.LibraryController import LibraryController


class LibraryApplication:

    def __init__(self, controller):
        self._controller = controller

    def run(self):
        print("Welcome to the library application! I hope you will enjoy the road!")
        answer = input("If you want to continue, type yes!")
        while answer != "yes" and answer != "no":
            answer = input("yes / no")
        if answer == "no":
            self._controller.recreate()
        while True:
            try:
                opt = Command(input("Type a command. Press 'help' in order to see the commands: "))
                cmd = opt.getArg(0)
                if cmd == "help":
                    self.showMenu()
                elif cmd == "addbook".lower():
                    self._controller.addBook(opt.toAddBook(len(self._controller.getBooks())))
                elif cmd == "addclient".lower():
                    self._controller.addClient(opt.toAddClient())
                elif cmd == "removebook".lower():
                    self._controller.removeBook(int(opt.getArg(1)))
                elif cmd == "removeclient".lower():
                    self._controller.removeClient(int(opt.getArg(1)))
                elif cmd == "updateid".lower():
                    self._controller.updateClientId(int(opt.getArg(1)), int(opt.getArg(2)))
                elif cmd == "updatename".lower():
                    self._controller.updateClientName(int(opt.getArg(1)), opt.getArg(2))
                elif cmd == "updatetitle".lower():
                    self._controller.updateTitle(int(opt.getArg(1)), opt.getArg(2))
                elif cmd == "updatedescription".lower():
                    self._controller.updateDescription(int(opt.getArg(1)), opt.getArg(2))
                elif cmd == "updateauthor".lower():
                    self._controller.updateAuthor(int(opt.getArg(1)), opt.getArg(2))
                elif cmd == "listbooks".lower():
                    print('\n\n'.join(str(book) for book in self._controller.getBooks()))
                elif cmd == "listclients".lower():
                    print('\n\n'.join(str(client) for client in self._controller.getClients()))
                elif cmd == "listloans".lower():
                    print('\n\n'.join(str(loan) for loan in self._controller.getLoans()))
                elif cmd == "list":
                    print(self._controller.getLibrary())
                elif cmd == "rentbook".lower():
                    self._controller.rentBook(int(opt.getArg(1)), int(opt.getArg(2)))
                elif cmd == "returnbook".lower():
                    self._controller.returnBook(int(opt.getArg(1)), int(opt.getArg(2)))
                elif cmd == "exit":
                    print("Quiting the app...")
                    break
                elif cmd == "delete":
                    self._controller.recreate()
                elif cmd == "save":
                    self._controller.save()
                else:
                    print("Command not recognized!")
            except ValueError as ve:
                print("ValueError - Argument should be integer!")
            except LibraryException as le:
                print(str(le))

    def showMenu(self):
        #Print all the available commands.

        print("Here are the commands:")
        print("     'addbook|Title|Description|Author'")
        print("     'addClient|Id|Name'")
        print("     'removeBook|ID'")
        print("     'removeClient|Id'")
        print("     'updateId|ACTUAL_Id|NEW_Id'")
        print("     'updateName|Id|NEW_NAME'")
        print("     'updateTitle|ID_BOOK|NEW_TITLE'")
        print("     'updateDescription|ID_BOOK|NEW_DESC'")
        print("     'updateAuthor|ID_BOOK|NEW_AUTH'")
        print("     'listBooks'")
        print("     'listClients'")
        print("     'listLoans'")
        print("     'rentBook|Id|BOOK_ID'")
        print("     'returnBOOK|Id|BOOK_ID'")
        print("     'delete'")
        print("     'save'")
        print("     'exit'")