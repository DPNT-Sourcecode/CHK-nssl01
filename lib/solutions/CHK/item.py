from typing import Optional
from functools import partial

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
        if deal:
            self.deal = partial(deal, self)
        
        if effect:
            self.effect = partial(effect, self)

    def run_deal(self):
        return self.deal(self)



