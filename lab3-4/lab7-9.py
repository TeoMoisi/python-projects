class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

    def print_all_options(self):
        print("        1. Afisare studenti \n\
        2. Adauga student \n\
        3. Afisare discipline \n\
        4. Adauga disciplina \n\
        5. Stergerea unui student cu id-ul dat \n\
        6. Asignare nota unui student la o disciplina \n\
        7. Modificarea notei unui student la o disciplina \n\
        8. Stergerea unei discipline cu id-ul dat \n\
        9. Modificarea unei discipline \n\
        10. Cautarea unui student \n\
        11. Afisarea studentilor cu note asignate \n\
        12. Afisarea studentilor si a notelor lor la o disciplina data, ordonati alfabetic dupa nume")

    def run(self):
        while True:
            self.print_all_options()
            options = {1: self.print_students, 2: self.add_students, 3: self.print_disciplines, 4: self.add_disciplines,
                       5: self.delete_student,
                       8: self.delete_discipline, 9: self.discipline_change, 10: self.find_student}
            try:
                op = int(input("Dati optiunea: "))
            except ValueError:
                print("Optiune gresita")
                return
            options[op]()
