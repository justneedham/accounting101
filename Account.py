from Transaction import Transaction


class Account(object):

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.inventory = 0
        self.transactions = list()

    def create_transaction(self, party, amount, total_amount, date, type):
        self.transactions.append(Transaction(party=party, amount=amount, total_amount=total_amount, date=date, type=type))