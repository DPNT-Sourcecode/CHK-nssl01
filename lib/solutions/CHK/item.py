from typing import Optional
from functools import partial

# An effect is anything that changes the price of something other than itself
# Deals are anything that changes that price of itself
# It seems that effects should run before deals
class Item:
    def __init__(self,
                 price: int,
                 amount: int = 0,
                 effect: Optional[callable] = None,
        ) -> None:
        self.price = price
        self.amount = amount

    def get_total_price(self):
        if self.deal != None:
            return self.deal()
        else:
            return self.price * self.amount
        

            def __init__(self, deals: List[Price]):
        self.deals = deals

    def get_price(self):
        self.deals.sort(key=lambda x: x.amount)
        total = 0
        amount = item.amount
        
        for deal in self.deals:
            current_deal = amount // deal.amount
            total += current_deal * item.price
            amount -= current_deal * deal.amount

        total += amount * item.price

        return total
