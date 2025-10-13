
# todo: Crea una clase cuenta con metodos depositar, retirar, mostrar_saldo.

class Account():
    def __init__(self, title, balance):
        self.title = title
        self.__balance = balance  # ? Atributo privados

    def deposit(self, mount):
        self.__balance += mount

    def withdraw(self, mount):
        if mount <= self.__balance:
            self.__balance -= mount
        else:
            print(f"Insufficient founds")

    def show_balance(self):
        print(f"Current balances: ${self.__balance}")


account = Account("Didier", 250000)
account.deposit(1000000)
account.show_balance()
account.withdraw(150000)
account.show_balance()
