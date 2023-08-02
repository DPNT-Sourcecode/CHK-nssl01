from typing import Optional

# An effect is anything that changes the price of something other than itself
# Deals are anything that changes that price of itself
# It seems that effects should run before deals
class Item:
    def __init__(self,
                 price: int,
                 amount: Optional[int] = 0,
                 deal: Optional[callable] = None,
                 effect: Optional[callable] = None,
        ) -> None:
        self.price = price
        self.amount = amount
        self.deal = deal
        self.effect = effect

    def run_deal(self):
        re

