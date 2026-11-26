class CreditAccount:
    def __init__(self, balance=0):
        self.balance = balance
        self.history = []

    def __add__(self, x):
        a = CreditAccount(self.balance + x)
        a.history = self.history + [f"+{x} кредитов"]
        return a

    def __sub__(self, x):
        if x > self.balance:
            raise ValueError("Не хватает кредитов! Иди подзаработай!")
        a = CreditAccount(self.balance - x)
        a.history = self.history + [f"-{x} кредитов"]
        return a

    def __mul__(self, x):
        self.balance += self.balance * x // 100
        self.history.append(f"*{x} (инвестиционный доход)")
        return self

    def __str__(self):
        return f"Баланс: {self.balance} кредитов"

    def show_history(self):
        for s in self.history:
            print(s)
