from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Price:
    amount: int
    price: int


class Item:
    def __init__(
        self,
        prices: List[Price],
        amount: int = 0,
    ) -> None:
        self.prices = prices
        self.amount = amount

    def get_price(self):
        self.prices.sort(key=lambda x: x.amount, reverse=True)
        total = 0
        amount = self.amount

        for price in self.prices:
            current_deal = amount // price.amount
            total += current_deal * price.price
            amount -= current_deal * price.amount

        return total
