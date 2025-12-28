account = {
    "balance": 1_000_000,
    "iban": "TR1",
    "status": "ACTIVE"
}

def get_balance():
    return account["balance"]


def withdraw(amount):
    account["balance"] -= amount

def deposit(amount):
    account["balance"] += amount

print(get_balance())
withdraw(10_000)
print(get_balance())
account["balance"] -= 10_000_000
print(get_balance())
