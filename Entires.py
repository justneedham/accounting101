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


company_name = "Alexandria / Sebastian Wolf Suits Consolidated"
tax_rate = .35
beginning_cash_bal = 10298.45
beginning_ar_bal = 0
beginning_inv_bal_sws = 0
beginning_inv_bal_alex = 0
beginning_ap_bal = 0
beginning_retained_earnings = 12122.45

# Functions for Income Statement


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

def print_income_statement():

    gross_margin = total_sales_rev() - total_cogs()
    income_before_taxes = gross_margin - total_admin_exp()

    print("2018 First Quarter Income Statement for {}".format(company_name))
    print("------------------------------")

    print("Sales Revenue:       ${}".format(total_sales_rev()))

    print("Cost of Goods Sold:  ${}".format(total_cogs()))

    print("Gross Margin:        ${}".format(gross_margin))

    print ("Admin Expenses:      ${}".format(total_admin_exp()))

    print("Income Before Taxes: ${}".format(income_before_taxes))

    print("Income Taxes:        ${}".format(income_taxes()))

    print("Net Income:          ${}".format(net_income()))
    print("------------------------------")


#Functions for Balance Sheet

def cash():
    change_in_cash = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "CASH":
            change_in_cash += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "CASH":
            change_in_cash -= entry.amount

    ending_cash_bal = change_in_cash + beginning_cash_bal
    return ending_cash_bal


def accounts_receivable():

    change_in_ar = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "A/R":
            change_in_ar += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "A/R":
            change_in_ar -= entry.amount

    ending_ar_bal = change_in_ar + beginning_ar_bal

    return ending_ar_bal


def inventory_sws():
    change_in_inv_sws = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "INV (SWS)":
            change_in_inv_sws += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "INV (SWS)":
            change_in_inv_sws -= entry.amount

    ending_inv_bal_sws = change_in_inv_sws + beginning_inv_bal_sws

    return ending_inv_bal_sws


def inventory_alex():
    change_in_inv_alex = 0

    for entry in data:
        if entry.type == "DEBIT" and entry.account_id == "INV (BOOKS)":
            change_in_inv_alex += entry.amount
        if entry.type == "CREDIT" and entry.account_id == "INV (BOOKS)":
            change_in_inv_alex -= entry.amount

    ending_inv_bal_alex = change_in_inv_alex + beginning_inv_bal_alex

    return ending_inv_bal_alex


def accounts_payable():
    change_in_ap = 0

    for entry in data:
        if entry.type == "CREDIT" and entry.account_id == "A/P":
            change_in_ap += entry.amount
        if entry.type == "DEBIT" and entry.account_id == "A/P":
            change_in_ap -= entry.amount

    ending_ap_bal = change_in_ap + beginning_ap_bal

    return ending_ap_bal


def retained_earnings():

    return beginning_retained_earnings


def print_balance_sheet():
    total_assets = cash() + accounts_receivable() + inventory_sws() + inventory_alex()
    total_liabilities = accounts_payable()
    total_equity = retained_earnings()
    total_liabilities_and_equity = total_liabilities + total_equity
    print(company_name)
    print("Balance Sheet for the year ending 2018")
    print("------------------------------")
    print("Current Assets")
    print("Cash:                ${}".format(cash()))
    print("A/R:                 ${}".format(accounts_receivable()))
    print("Inventory (SWS):     ${}".format(inventory_sws()))
    print("Inventory (Alex)     ${}".format(inventory_alex()))
    print("Total Assets:        ${}".format(total_assets))
    print("")
    print("Current Liabilities")
    print("Accounts Payable:    ${}".format(accounts_payable()))
    print("")
    print ("Owners Equity")
    print("Retained Earnings:   ${}".format(retained_earnings()))
    print("")
    print("liabilities/equity:  ${}".format(total_liabilities_and_equity))
    print("------------------------------")




print("Total debits are credits equal: {}".format(total_debs_and_creds()))
print("")

print("Here is the first quarter income statement: ")
print("")

print_income_statement()
print("")

print_balance_sheet()
