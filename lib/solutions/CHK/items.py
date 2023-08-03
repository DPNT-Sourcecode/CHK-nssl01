from dataclasses import dataclass
from typing import List
from solutions.CHK.item import Item

@dataclass
class Offer:
    amount: int
    price: int

class Deal():
    def __init__(self, deals: List[Offer]):
        self.deals = deals

    def build(self, item: Item):
        sorted_by_amount = self.deals.sort(key=)

def a_deal(self: Item) -> int:
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

def b_deal(self: Item) -> int:
        amount = self.amount
        total = 0

        b_deals = (amount // 2)
        total += b_deals * 45
        total += (amount % 2) * self.price

        return total

def f_deal(self: Item) -> int:
    n_to_remove = self.amount // 3
    amount = self.amount - n_to_remove
    
    return amount * self.price

def h_deal(self: Item) -> int:
    amount = self.amount
    total = 0

    h_10_deals = amount // 10
    total += h_10_deals * 80
    amount -= h_10_deals * 10

    a_5_deals = (amount // 5)
    total += a_5_deals * 45
    amount -= a_5_deals * 5

    total += amount * self.price

    return total

def k_deal(self: Item) -> int:
    amount = self.amount
    total = 0

    b_deals = (amount // 2)
    total += b_deals * 150
    total += (amount % 2) * self.price

    return total

def k_deal(self: Item) -> int:
    amount = self.amount
    total = 0

    b_deals = (amount // 2)
    total += b_deals * 150
    total += (amount % 2) * self.price

    return total

# Takes 'Shop'
def e_effect(self) -> None:
    if "E" in self.items and "B" in self.items:
        b_amount = self.get_amount("B")
        e_amount = self.get_amount("E")
        b_amount_after_bogo = b_amount - (e_amount // 2)

        # No minus amounts
        self.items["B"].amount = max(0, b_amount_after_bogo)


# 3N get one M free
def n_effect(self) -> None:
    if "N" in self.items and "M" in self.items:
        affected_amount = self.get_amount("M")
        effect_amount = self.get_amount("N")
        amount_after_bogo = affected_amount - (effect_amount // 3)

        # No minus amounts
        self.items["M"].amount = max(0, amount_after_bogo)


items = {
    "A": lambda amount = 0: Item(50, amount, deal=a_deal),
    "B": lambda amount = 0: Item(30, amount, deal=b_deal),
    "C": lambda amount = 0: Item(20, amount),
    "D": lambda amount = 0: Item(15, amount),
    "E": lambda amount = 0: Item(40, amount, effect=e_effect),
    "F": lambda amount = 0: Item(10, amount, deal=f_deal),
    "G": lambda amount = 0: Item(20, amount),
    "H": lambda amount = 0: Item(10, amount, deal=h_deal),
    "I": lambda amount = 0: Item(35, amount),
    "J": lambda amount = 0: Item(60, amount),
    "K": lambda amount = 0: Item(80, amount, deal=k_deal),
    "L": lambda amount = 0: Item(90, amount),
    "M": lambda amount = 0: Item(15, amount),
    "N": lambda amount = 0: Item(40, amount, effect=n_effect),
    "O": lambda amount = 0: Item(10, amount),
    "P": lambda amount = 0: Item(50, amount),
    "Q": lambda amount = 0: Item(30, amount),
    "R": lambda amount = 0: Item(50, amount),
    "S": lambda amount = 0: Item(30, amount),
    "T": lambda amount = 0: Item(20, amount),
    "U": lambda amount = 0: Item(40, amount),
    "V": lambda amount = 0: Item(50, amount),
    "W": lambda amount = 0: Item(20, amount),
    "X": lambda amount = 0: Item(90, amount),
    "Y": lambda amount = 0: Item(10, amount),
    "Z": lambda amount = 0: Item(50, amount)
}







