from Transaction import Transaction


class Account(object):

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.inventory = 0
        self.transactions = list()

    def create_transaction(self, **kwargs):
        self.transactions.append(
            Transaction(
                party=kwargs['party'],
                amount=kwargs['amount'],
                total_amount=kwargs['total_amount'],
                date=kwargs['date'],
                type=kwargs['type'],
                first_cost=kwargs['first_cost'],
            ))

    def get_total(self):
        total_amount = 0
        for transaction in self.transactions:
            total_amount += transaction.amount

        print(total_amount)
