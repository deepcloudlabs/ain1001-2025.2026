from functools import reduce

accounts = [
    {"iban": "TR1", "balance": 10_000, "status": "ACTIVE"},
    {"iban": "TR2", "balance": 20_000, "status": "CLOSED"},
    {"iban": "TR3", "balance": 30_000, "status": "ACTIVE"},
    {"iban": "TR4", "balance": 40_000, "status": "BLOCKED"},
    {"iban": "TR5", "balance": 50_000, "status": "ACTIVE"},
]

total = 0
for account in accounts:
    if account["status"] == "ACTIVE":
        total += account["balance"]
print(total)
if_active_account = lambda account: account["status"] == "ACTIVE"
to_balance = lambda account: account["balance"]
to_sum = lambda a, b: a + b
total = reduce(to_sum, map(to_balance, filter(if_active_account, accounts)), 0)
print(total)
