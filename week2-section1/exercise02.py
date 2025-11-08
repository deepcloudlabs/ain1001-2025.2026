from functools import reduce

accounts = [
    {"iban": "tr1", "balance": 100_000, "status": "active"},
    {"iban": "tr2", "balance": 200_000, "status": "closed"},
    {"iban": "tr3", "balance": 300_000, "status": "blocked"},
    {"iban": "tr4", "balance": 400_000, "status": "active"},
    {"iban": "tr5", "balance": 500_000, "status": "active"}
]
active_accounts = 0
for account in accounts:
    if account["status"] == "active":
        active_accounts += 1
print(active_accounts)
if_active = lambda account: account["status"] == "active"
to_1 = lambda account: 1
to_sum = lambda x, y: x + y
active_accounts = reduce(to_sum,
                         map(to_1,
            filter(if_active, accounts)), 0)
print(active_accounts)
