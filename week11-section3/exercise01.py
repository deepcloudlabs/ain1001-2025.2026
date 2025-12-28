account = {
    "iban": "TR1",
    "balance": 1_000_000,
    "status": "ACTIVE"
}

def deposit(amount: float) -> None:
    account["balance"] += amount

def withdraw(amount: float) -> bool:
    if amount > account["balance"]:
        return False
    account["balance"] -= amount
    return True

def get_balance() -> float:
    return account["balance"]

withdraw(10_000)
deposit(200_000)
print(get_balance())
account["balance"] -= 100_000_000
print(get_balance())
