from typing import Optional

# noinspection PyUnusedLocal
# skus = unicode string

# 3A for 130
# 2B for 45
prices = {
    "A": 50,
    "B": 30,
    "C": 20,
    "D": 15,
    "E": 40,
}

class Item:
    def __init__(self, price: int, amount: int) -> None:
        self.price = price
        self.amount = amount

    def total_price(self) -> int:
        return self.price * self.amount
        

class ItemA():
    def __init__(self, amount: int) -> None:
        self.amount = amount
        self.price = 50

    def total_price(self) -> int:
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

class ItemB():
    def __init__(self, amount: int) -> None:
        self.amount = amount
        self.price = 50

    def total_price(self) -> int:
        amount = self.amount
        total = 0

        b_deals = (amount // 2)
        total += b_deals * 45
        total += (amount % 2) * prices["B"]

        return total

class ItemC(Item):
    def __init__(self, amount: int) -> None:
        super().__init__(20, amount)

class ItemD(Item):
    def __init__(self, amount: int) -> None:
        super().__init__(15, amount)

class ItemE(Item):
    def __init__(self, amount: int) -> None:
        super().__init__(40, amount)

def checkout(skus: str) -> int:
    if type(skus) != str:
        print("Wrong type")
        return -1
    
    # Anything but A, B, C, or D is invalid
    valid = prices.keys()
    for sku in skus:
        if sku not in valid:
            print("Invalid SKU")
            return -1
        
    count = {}

    for sku in skus:
        if sku in count:
            count[sku] += 1
        else:
            count[sku] = 1


    a_total = ItemA(count.get("A", 0)).total_price()
    c_total = ItemC(count.get("C", 0)).total_price()
    d_total = ItemD(count.get("D", 0)).total_price()
    e_total = ItemE(count.get("E", 0)).total_price()

    b_amount_after_bogo = 
    b_total = ItemB(count.get("B", 0)).total_price()
    # Total cost of of buy-one-get-ones to minus from 
    if "E" in count:
        b_bogo_to_minus = (ItemB(count["E"] // 2).total_price())
        b_total -= b_bogo_to_minus
        if b_total < 0:
            b_total = 0

    return a_total + b_total + c_total + d_total + e_total




