

class Entry(object):

    def __init__(self, type, amount, account, date):
        self.type = type  # 'debit'
        self.amount = amount  # decimal
        self.account_id = account  # string CASH, COGS, REV, A/R, A/P, Sales Tax, Inv
        self.data = date  # '01-01-18'

