
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        print("okay")

    def make_withdrawal(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance} ")

an = User("Bob")
ok = User("Sydney")
an.make_withdrawal(100)

an.display_user_balance()
class User:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        print("okay")

    def make_withdrawal(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.balance} ")

an = User("Bob")
ok = User("Sydney")
get = User("Chris")

an.make_withdrawal(100)
ok.make_withdrawal(350)
get.make_withdrawal(250)

an.display_user_balance()
ok.display_user_balance()
get.display_user_balance()