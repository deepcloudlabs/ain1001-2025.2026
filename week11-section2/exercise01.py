from enum import Enum


class AccountStatus(Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"


class InactiveAccountError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class Account:
    def __init__(self, iban: str, balance: float = 0.0, status: AccountStatus = AccountStatus.ACTIVE) -> None:
        # field, attribute, state, property
        self.__iban = iban
        self.__balance = balance
        self.__status = status

    def __str__(self) -> str:
        return f"Account [iban: {self.__iban}, balance: {self.__balance}, status: {self.__status}]"

    @property
    def iban(self) -> str:
        return self.__iban

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def status(self) -> AccountStatus:
        return self.__status

    @status.setter
    def status(self, status: AccountStatus):
        if status not in AccountStatus:
            raise ValueError(f"{status} is not accepted")
        self.__status = status

    def deposit(self, amount: float) -> float:
        if self.__status != AccountStatus.ACTIVE:
            raise InactiveAccountError(f"This is not an active account: {self.__status}")
        if amount <= 0.0:  # validation
            raise ValueError("Amount must be positive")
        self.__balance = self.__balance + amount
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if self.__status != AccountStatus.ACTIVE:
            raise InactiveAccountError(f"This is not an active account: {self.__status}")
        if amount <= 0.0:  # validation
            raise ValueError("Amount must be positive")
        if amount > self.__balance:  # business rule
            raise ValueError("Amount cannot be greater than the balance")
        self.__balance = self.__balance - amount
        return self.__balance

acc1 = Account("TR1", 1_000_000.0, AccountStatus.ACTIVE)
try:
    print(str(acc1))
    acc1.withdraw(2_000_000)
    print(acc1.balance)
    # acc1.balance = acc1.balance - 2_000_000
    print(acc1.status)  # read the property
    acc1.status = "asdadsa"  # write to the property
    print(acc1.status)
except InactiveAccountError as e:
    print(str(e))
except ValueError as e:
    print(str(e))
finally:
    print(str(acc1))