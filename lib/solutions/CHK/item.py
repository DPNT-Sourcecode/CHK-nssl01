from dataclasses import dataclass
from typing import List, Optional



@dataclass
class Price:
    amount: int
    price: int

# An effect is anything that changes the price of something other than itself
# Deals are anything that changes that price of itself
# It seems that effects should run before deals
class Item:
    def __init__(self,
                 prices: List[Price],
                 amount: int = 0,
                 effect: Optional[callable] = None,
        ) -> None:
        self.prices = prices
        self.amount = amount
        self.effect = effect

    def get_price(self):
        self.prices.sort(key=lambda x: x.amount)
        total = 0
        amount = self.amount
        
        for price in self.prices:
            current_deal = amount // price.amount
            total += current_deal * price.price
            amount -= current_deal * price.amount

        return total

