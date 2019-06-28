class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, filepath, fees):
        Account.__init__(self, filepath)
        self.fees = fees

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fees


checking = Checking("balance", 5)
# checking.deposit(10)
checking.transfer(110)
print(checking.balance)
checking.commit()