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
    def __init__(self, price: int, amount: int, deal: Optional[callable] = None) -> None:
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
    def __init__(self, price: int, amount: int, deal: Any | None = None) -> None:
        super().__init__(price, amount, )

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

    total = 0



    a = Item(count.get("A", 0))

    
    if "A" in count:
        a = count["A"]



    if "B" in count:
        ...


    if "C" in count:
        total += count["C"] * prices["C"]

    if "D" in count:
        total += count["D"] * prices["D"]

    if "E" in count:
        e = count["E"]
        e_bogo = (e // 2)

        # we only want to make as many Bs free as we have
        # didn't factor in deals from b, don't want to give away money
        if "B" in count:
            if count["B"] < e_bogo:
                total -= count["B"] * prices["B"]
            else:
                total -= e_bogo * prices["B"]

        total += count["E"] * prices["E"]

    return total









