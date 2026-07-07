import csv


def load_accounts():
    with open("accounts.csv", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def calculate_totals(accounts):
    totals = {}
    net_worth = 0

    for row in accounts:
        category = row["category"]
        balance = float(row["balance"])

        net_worth += balance
        totals[category] = totals.get(category, 0) + balance

    return net_worth, totals


def print_report(net_worth, totals):
    print()
    print(f"Net Worth: ${net_worth:,.2f}")

    for category, total in totals.items():
        percent = total / net_worth * 100
        print(f"{category}: ${total:,.2f} ({percent:.2f}%)")
    
    print()

def main():
    accounts = load_accounts()
    net_worth, totals = calculate_totals(accounts)
    print_report(net_worth, totals)


if __name__ == "__main__":
    main()

