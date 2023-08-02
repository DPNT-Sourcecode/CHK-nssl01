from typing import Optional
from solutions.CHK.shop import Shop

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

def a_deal(self) -> int:
    amount = self.amount
    total = 0

    a_5_deals = amount // 5
    total += a_5_deals * 200
    amount -= a_5_deals * 5

    a_3_deals = (amount // 3)
    total += a_3_deals * 130
    amount -= a_3_deals * 3

    total += amount * self.price

    return total

def e_effect(self: Shop) -> None:
    if self.items["E"] != 0 and self.items["B"] != 0:
        b_amount = self.get_amount("B")
        e_amount = self.get_amount("E")
        b_amount_after_bogo = b_amount - (e_amount // 2)
        self.items["B"].amount = b_amount_after_bogo

items = {
    "A": Item(50, deal=a_deal),
    "B": Item(30),
    "C": Item(20),
    "D": Item(15),
    "E": Item(40, effect=e_effect),
    "F": Item(10),
    "G": Item(20),
    "H": Item(10),
    "I": Item(35),
    "J": Item(60),
    "K": Item(80),
    "L": Item(90),
    "M": Item(15),
    "N": Item(40),
    "O": Item(10),
    "P": Item(50),
    "Q": Item(30),
    "R": Item(50),
    "S": Item(30),
    "T": Item(20),
    "U": Item(40),
    "V": Item(50),
    "W": Item(20),
    "X": Item(90),
    "Y": Item(10),
    "Z": Item(50)
}



