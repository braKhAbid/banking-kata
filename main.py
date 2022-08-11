import datetime
import datetime as dt


class Account:
    def __init__(self, initial):
        self.balance = 0
        self.history = []
        self.add_to_history(0, initial)
        self.balance = initial

    def deposit(self, amount):
        self.add_to_history(self.balance, amount)
        self.balance = self.balance + amount

    def withdraw(self, amount):
        self.add_to_history(self.balance, - amount)
        self.balance = self.balance - amount

    def add_to_history(self, current_balance, new):
        new_data = [datetime.date.today().strftime("%d.%m.%Y").ljust(15), new, current_balance + new]
        self.history.append(new_data)

    def printStatement(self):
        print("Date".ljust(15) + "Amount".ljust(10) + "Balance")
        for data in self.history:
            new_line = data[0] + self.format_amount(data[1]).ljust(10) + self.format_amount(data[2])
            print(new_line)

    def format_amount(self, amount):
        if amount < 0:
            return str(amount)
        else:
            return '+'+str(amount)

def print_hi(name):
    print('Hi, {}'.format(name))

if __name__ == '__main__':
    acc = Account(0)
    acc.deposit(100)
    acc.withdraw(200)
    acc.printStatement()

