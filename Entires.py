from Entry import Entry

data = [
    Entry(type="DEBIT", amount=349.50, account="CASH", date="01-02-18"), #Suit Sale
    Entry(type="DEBIT", amount=349.50, account="A/R", date="01-02-18"),
    Entry(type="CREDIT", amount=699.00, account="SALES REV", date="01-02-18"),
    Entry(type="DEBIT", amount=240.00, account="COGS", date="01-02-18"),
    Entry(type="CREDIT", amount=240.00, account="A/P", date="01-02-18"),
    Entry(type="DEBIT", amount=349.50, account="CASH", date="01-12-18"), #Collection from suit sale
    Entry(type="CREDIT", amount=349.50, account="A/R", date="01-12-18"),
    Entry(type="DEBIT", amount=299.50, account="CASH", date="01-23-18"), #Suit Sale 2
    Entry(type="DEBIT", amount=299.50, account="A/R", date="01-23-18"),
    Entry(type="CREDIT", amount=599.00, account="SALES REV", date="01-23-18"),
    Entry(type="DEBIT", amount=210.00, account="COGS", date="01-23-18"),
    Entry(type="CREDIT", amount=210.00, account="A/P", date="01-23-18"),
    Entry(type="DEBIT", amount=400.00, account="A/P", date="01-23-18"), #Pay Chang Gae
    Entry(type="CREDIT", amount=400.00, account="CASH", date="01-23-18"),
    Entry(type="DEBIT", amount=349.50, account="CASH", date="01-25-18"), #Suit Sale 3
    Entry(type="DEBIT", amount=349.50, account="A/R", date="01-25-18"),
    Entry(type="CREDIT", amount=699.00, account="SALES REV", date="01-25-18"),
    Entry(type="DEBIT", amount=240.00, account="COGS", date="01-25-18"),
    Entry(type="CREDIT", amount=240.00, account="A/P", date="01-25-18"),
    Entry(type="DEBIT", amount=1829.03, account="INV (SWS)", date="02-05-18"), #Purchase Ties
    Entry(type="CREDIT", amount=1829.03, account="CASH", date="02-05-18"),
    Entry(type="DEBIT", amount=50.00, account="CASH", date="02-07-18"), #Tie Sale 1
    Entry(type="CREDIT", amount=50.00, account="SALES REV", date="02-07-18"),
    Entry(type="DEBIT", amount=8.00, account="COGS", date="02-07-18"),
    Entry(type="CREDIT", amount=8.00, account="INV (SWS)", date="02-07-18"),
    Entry(type="DEBIT", amount=125.00, account="CASH", date="02-15-18"), #Tie Sale 2
    Entry(type="CREDIT", amount=125.00, account="SALES REV", date="02-15-18"),
    Entry(type="DEBIT", amount=20.00, account="COGS", date="02-15-18"),
    Entry(type="CREDIT", amount=20.00, account="INV (SWS)", date="02-15-18"),
    Entry(type="DEBIT", amount=50.00, account="INV (BOOKS)", date="03-01-18"), #Buy Books 1
    Entry(type="CREDIT", amount=50.00, account="CASH", date="03-01-18"),
    Entry(type="DEBIT", amount=200.00, account="INV (BOOKS)", date="03-05-18"), #Buy Books 2 & 3
    Entry(type="CREDIT", amount=200.00, account="CASH", date="03-05-18"),
    Entry(type="DEBIT", amount=300.00, account="CASH", date="03-17-18"), #Sell a Book
    Entry(type="CREDIT", amount=300.00, account="SALES REV", date="03-17-18"),
    Entry(type="DEBIT", amount=50.00, account="COGS", date="03-17-18"),
    Entry(type="CREDIT", amount=50.00, account="INV (BOOKS)", date="03-17-18"),
    Entry(type="DEBIT", amount=200.00, account="CASH", date="03-20-18"), #sell a Book 2
    Entry(type="CREDIT", amount=200.00, account="SALES REV", date="03-20-18"),
    Entry(type="DEBIT", amount=120.00, account="COGS", date="03-20-18"),
    Entry(type="CREDIT", amount=120.00, account="INV (BOOKS)", date="03-20-18"),
    Entry(type="DEBIT", amount=50.00, account="ADMIN EXP", date="03-21-18"), #Renew Website
    Entry(type="CREDIT", amount=50.00, account="CASH", date="03-21-18"),
    Entry(type="DEBIT", amount=80.00, account="ADMIN EXP", date="03-28-18"), #Renew Business License
    Entry(type="CREDIT", amount=80.00, account="CASH", date="03-28-18"),
]



# functions for Income Statement

tax_rate = .35


def total_debs_and_creds():

    total_debits = 0
    total_credits = 0

    for entry in data:

        if entry.type == "DEBIT":
            total_debits += entry.amount
        if entry.type == "CREDIT":
           total_credits += entry.amount

    totaldc = total_debits - total_credits
    return totaldc


def total_sales_rev():

    total_sales_rev = 0

    for entry in data:

        if entry.type == "CREDIT" and entry.account_id == "SALES REV":
            total_sales_rev += entry.amount
        if entry.type == "DEBIT" and entry.account_id == "SALES REV":
            total_sales_rev -= entry.amount
    return total_sales_rev


def total_cogs():

    total_cogs = 0

    for entry in data:

        if entry.type == "DEBIT" and entry.account_id == "COGS":
            total_cogs += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "COGS":
            total_cogs -= entry.amount
    return total_cogs


def total_admin_exp():

    total_admin_exp = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "ADMIN EXP":
            total_admin_exp += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "ADMIN EXP":
            total_admin_exp += entry.amount
    return total_admin_exp


def income_taxes():
    income_tax_owed = (tax_rate * income_before_taxes)
    return income_tax_owed


def net_income():

    net_income = (1-tax_rate) * income_before_taxes
    return net_income



gross_margin = total_sales_rev() - total_cogs()
income_before_taxes = gross_margin - total_admin_exp()



print(total_debs_and_creds())
print("")

print("Sales Revenue:       ${}".format(total_sales_rev()))

print("Cost of Goods Sold:  ${}".format(total_cogs()))


print("Gross Margin:        ${}".format(gross_margin))

print ("Admin Expenses:      ${}".format(total_admin_exp()))

print("Income Before Taxes: ${}".format(income_before_taxes))

print("Income Taxes:        ${}".format(income_taxes()))

print("Net Income:          ${}".format(net_income()))





























