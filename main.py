import csv

totals = {}
net_worth = 0

with open("accounts.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        category = row["category"]
        balance = float(row["balance"])

        net_worth += balance
        totals[category] = totals.get(category, 0) + balance

print(f"Net Worth: ${net_worth:,.2f}")
print()

for category, total in totals.items():
    percent = total / net_worth * 100
    print(f"{category}: ${total:,.2f} ({percent:.2f}%)")
