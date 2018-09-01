from Account import Account


data = [
    {'PARTY': 'Justin',
     'AMOUNT': 599.99,
     'TOTAL_AMOUNT': 599.99,
     'FIRST_COST': 199.99,
     'DATE': '08-02-28',
     'TYPE': 'ORDER',
     },
    {'PARTY': 'Justin',
     'AMOUNT': 599.99,
     'TOTAL_AMOUNT': 599.99,
     'FIRST_COST': 199.99,
     'DATE': '08-02-28',
     'TYPE': 'ORDER',
     },
    {'PARTY': 'Justin',
     'AMOUNT': 599.99,
     'TOTAL_AMOUNT': 599.99,
     'FIRST_COST': 199.99,
     'DATE': '08-02-28',
     'TYPE': 'ORDER',
     },
]


class Controller(object):

    def __init__(self):
        self.account = Account('Sebastian Wolf', 1000)

    def run(self, data):
        for transaction in data:
            self.account.create_transaction(
                party=transaction['PARTY'],
                amount=transaction['AMOUNT'],
                total_amount=transaction['TOTAL_AMOUNT'],
                date=transaction['DATE'],
                type=transaction['TYPE'],
                first_cost=transaction['FIRST_COST']
            )

        for transaction in self.account.transactions:
            print(transaction.party, transaction.amount, transaction.date)


if __name__ == '__main__':
    app = Controller()
    app.run(data)



