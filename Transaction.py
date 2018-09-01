from Entry import Entry


class Transaction(object):

    sales_tax_rate = 0.0685

    def __init__(self, **kwargs):
        self.party = kwargs['party']
        self.amount = kwargs['amount']
        self.total_amount = kwargs['total_amount']
        self.date = kwargs['date']
        self.type = kwargs['type']
        self.first_cost = kwargs['first_cost']
        self.sales_tax_ind = kwargs['sales_tax_ind']
        self.location = "Malibu"
        self.status = "pending"
        self.balance_sheet_entries = list()
        self.income_statement_entries = list()

    def create_entries(self):
        if self.type == 'ORDER':
            self.income_statement_entries.extend((
                Entry(
                    type='CREDIT',
                    amount=self.amount - (self.amount * self.sales_tax_rate),
                    account='REV',
                    date=self.date
                ),
                Entry(
                    type='CREDIT',
                )
            ))
            self.balance_sheet_entries.extend((

            ))



            self.entries.extend((
                Entry(
                    type='DEBIT',
                    amount=self.amount,
                    account='CASH',
                    date=self.date
                ),
                Entry(
                    type='DEBIT',
                    amount=self.first_cost,
                    account='COGS',
                    date=self.date
                ))
            )










