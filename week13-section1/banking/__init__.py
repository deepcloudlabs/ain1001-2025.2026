from enum import Enum


class InsufficientBalanceException(Exception):
    def __init__(self, message: str, deficit: float):
        super().__init__(message)
        self.deficit = deficit

class AccountStatus(Enum):
    ACTIVE = "ACTIVE"
    BLOCKED = "BLOCKED"
    CLOSED = "CLOSED"

class Account:
    def __init__(self, iban: str, balance: float, status: AccountStatus):
        self.__iban = iban
        self.__balance = balance
        self.__status = status

    def __str__(self):
        return f"Account[ iban: {self.__iban}, balance: {self.__balance}, status: {self.__status}]"

    @property
    def balance(self) -> float:
        return self.__balance

    @property
    def iban(self) -> str:
        return self.__iban

    @property
    def status(self) -> AccountStatus:
        return self.__status

    @status.setter
    def status(self, value: AccountStatus):
        if value in AccountStatus:
            self.__status = value


    def deposit(self, amount: float) -> float:
        if amount <= 0:  # validation rule
            raise ValueError("amount must be positive")
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:  # validation rule
            raise ValueError("amount must be positive")
        if amount > self.__balance:  # business rule
            raise InsufficientBalanceException("Your balance does not cover your expenses",amount-self.__balance)
        self.__balance -= amount
        return self.__balance
