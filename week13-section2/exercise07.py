from banking import Account, InactiveAccountError, AccountStatus

acc1 = Account("TR1", 1_000_000.0, AccountStatus.ACTIVE)
try:
    print(str(acc1))
    acc1.withdraw(2_000_000)
    print(acc1.balance)
    # acc1.balance = acc1.balance - 2_000_000
    print(acc1.status)  # read the property
    acc1.status = AccountStatus.ACTIVE  # write to the property
    print(acc1.status)
except InactiveAccountError as e:
    print(str(e))
except ValueError as e:
    print(str(e))
finally:
    print(str(acc1))