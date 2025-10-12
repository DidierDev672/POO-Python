class BankAccount:
    def __init__(self, title,  balance):
        self.title = title
        self.__balance = balance  # ? Atributo privado

    def deposit(self, mount):
        self.__balance += mount

    def withdraw(self, mount):
        if mount <= self.__balance:
            self.__balance -= mount
        else:
            print(f"Insufficient funds")

    def show_balance(self):
        print(f"Current balances: ${self.__balance}")


account = BankAccount("Ana", 1000)
account.deposit(500)
account.show_balance()
account.withdraw(2000)
