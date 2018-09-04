from Entry import Entry

data = [
    Entry(type="CREDIT", amount=1000, account="SALES REV", date="01-02-18"),
    Entry(type="DEBIT", amount=500, account="COGS", date="01-02-18"),
    Entry(type="DEBIT", amount=200, account="COGS", date="01-02-18"),
]


# functions for Income Statement


def total_debs_and_creds():

    total_debits = 0
    total_credits = 0

    for entry in data:

        if entry.type == "DEBIT":
            total_debits += entry.amount
        if entry.type == "CREDIT":
           total_credits += entry.amount

    totaldc = total_credits - total_debits
    return totaldc


def total_cogs():

    total_cogs = 0

    for entry in data:

        if entry.type == "DEBIT" and entry.account_id == "COGS":
            total_cogs += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "COGS":
            total_cogs -= entry.amount
    return total_cogs


def total_sales_rev():

    total_sales_rev = 0

    for entry in data:

        if entry.type == "CREDIT" and entry.account_id == "SALES REV":
            total_sales_rev += entry.amount
        if entry.type == "DEBIT" and entry.account_id == "SALES REV":
            total_sales_rev -= entry.amount
    return total_sales_rev


print(total_debs_and_creds())

print(total_cogs())

print(total_sales_rev())

gross_margin = total_sales_rev() - total_cogs()

print(gross_margin)
