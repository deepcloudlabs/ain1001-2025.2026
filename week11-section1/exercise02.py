from enum import Enum


class RegulationError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class InsufficientBalanceError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class AccountStatus(Enum):
    ACTIVE = "ACTIVE"
    CLOSED = "CLOSED"
    BLOCKED = "BLOCKED"


class Account:
    def __init__(self, iban: str, balance: float, status: AccountStatus):
        self.__iban = iban
        self.__balance = balance
        self.__status = status

    def __str__(self):
        return f"Account [iban: {self.__iban}, balance: {self.__balance}, status: {self.__status}]"

    @property
    def balance(self):
        return self.__balance

    @property
    def iban(self):
        return self.__iban

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status: AccountStatus):
        if status in AccountStatus:
            self.__status = status

    def deposit(self, amount: float) -> float:
        if self.__status != AccountStatus.ACTIVE:
            raise RegulationError("Cannot deposit inactive account")
        if amount <= 0.0:  # validation rules
            raise ValueError("Cannot deposit incorrect amount")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if self.__status != AccountStatus.ACTIVE:  # regulation
            raise RegulationError("Cannot deposit inactive account")
        if amount <= 0.0:  # validation rule
            raise ValueError("Cannot withdraw incorrect amount")
        if amount > self.__balance:  # business rule
            raise InsufficientBalanceError("Cannot cover your expenses")
        self.__balance -= amount
        return self.__balance

try:
    acc1 = Account("TR1", 1_000_000, status=AccountStatus.BLOCKED)
    acc1.deposit(500_000)
    acc1.withdraw(100_000_000)
    print(acc1.balance)
    # acc1.balance = acc1.balance - 100_000_000
    print(acc1.status)
    acc1.status = AccountStatus.CLOSED
    print(acc1.status)
    print(str(acc1))
except RegulationError as e:
    print(str(e))
except InsufficientBalanceError as e:
    print(str(e))
except ValueError as e:
    print(str(e))
finally:
    print("Application is done")