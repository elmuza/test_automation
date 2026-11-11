class BankAccount:
    def __init__(self, owner, balance=0):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть больше нуля")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть больше нуля")

        if amount > self.balance:
            raise ValueError("Недостаточно средств")

        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

    def transfer(self, target_account, amount):
        if amount <= 0:
            raise ValueError("Сумма перевода должна быть больше нуля")

        if amount > self.balance:
            raise ValueError("Недостаточно средств")

        self.withdraw(amount)
        target_account.deposit(amount)

        return self.balance