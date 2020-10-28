from typing import Dict, Optional


class CashFlow:

    def __init__(self, amount: float, n: int):
        self.amount = amount
        self.n = n

    def pv(self, r: float) -> 'CashFlow':
        return CashFlow(amount=self.amount * (1 + r) ** (-self.n), n=0)

    def fv(self, r: float) -> 'CashFlow':
        return CashFlow(amount=self.amount * (1 + r) ** self.n, n=self.n)

    def shift(self, n: int, r: float) -> 'CashFlow':
        return CashFlow(amount=self.amount * (1 + r) ** (-n), n=n)

    def merge(self, other: 'CashFlow', r: float, reverse: bool = False) -> 'CashFlow':
        raise NotImplementedError

    def to_dict(self, decimal_places: Optional[int] = 2) -> Dict:
        return {
            "amount": self.amount if decimal_places is None else round(self.amount, decimal_places),
            "n": self.n
        }
