from banking import Account, AccountStatus, InsufficientBalanceException

try:
    acc1 = Account("TR1", 1_000_000, AccountStatus.ACTIVE)
    acc1.withdraw(100_000_000)
    acc1.deposit(2_500_000)
    print(acc1.balance)
    print(str(acc1))
    #acc1.balance = acc1.balance - 100_000_000
    acc1.status = AccountStatus.CLOSED
    print(acc1)
    acc1.status = AccountStatus.BLOCKED
    print(acc1)
except InsufficientBalanceException as e:
    print(str(e))
except ValueError as e:
    print(str(e))
finally:
    print("Application is done")

