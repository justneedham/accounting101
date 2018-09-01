from Entry import Entry


class Transaction(object):

    def __init__(self, party, amount, total_amount, date, type, location='Malibu', status="pending"):
        self.amount = amount
        self.total_amount = total_amount
        self.location = location
        self.date = date
        self.type = type
        self.party = party
        self.status = status
        self.entries = []







