from Account import Account


data = [
    {'Party': 'Justin',
     'Amount': 599.99,
     'Total Amount': 599.99,
     'Date': '08-02-28',
     'Type': 'ORDER',
     },
    {'Party': 'Jace',
     'Amount': 499.99,
     'Total Amount': 599.99,
     'Date': '08-02-28',
     'Type': 'ORDER',
     },
    {'Party': 'Spencer',
     'Amount': 599.99,
     'Total Amount': 99.99,
     'Date': '08-02-28',
     'Type': 'ORDER',
     },
]


class Controller(object):

    def __init__(self):
        self.account = Account('Sebastian Wolf', 1000)

    def run(self, data):
        for transaction in data:
            self.account.create_transaction(
                transaction['Party'],
                transaction['Amount'],
                transaction['Total Amount'],
                transaction['Date'],
                transaction['Type'],
            )

        for transaction in self.account.transactions:
            print(transaction.party, transaction.amount, transaction.date)

        self.account.get_total()

if __name__ == '__main__':
    app = Controller()
    app.run(data)



