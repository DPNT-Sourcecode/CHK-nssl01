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
}

class Checkout:
    def __init__(self, skus) -> None:
        self.skus = skus

        count = {}
        for sku in skus:
            if sku in count:
                count[sku] += 1
            else:
                count[sku] = 1

        self.counts = count

    def get_count(self, sku: str) -> Optional[int]:
        return self.counts[sku]



class Item:
    def __init__(self, price, amount, deal: Optional[callable] = None) -> None:
        self.price: int = price
        self.amount: int = amount
        self.deal: callable = deal

    def get_price(self):
        if self.deal != None:
            return self.deal()
        else:
            return self.price * self.amount    


def checkout(skus: str) -> int:
    if type(skus) != str:
        return -1
    
    # Anything but A, B, C, or D is invalid
    valid = prices.keys()
    for sku in skus:
        if sku not in valid:
            return -1
        
    count = {}



    total = 0


    
    if "A" in count:
        a = count["A"]
        a_deals = (a // 3)
        total += a_deals * 130
        total += (a % 3) * 50

    if "B" in count:
        b = count["B"]
        b_deals = (b // 2)
        total += b_deals * 45
        total += (b % 2) * 30

    if "C" in count:
        total += count["C"] * 20

    if "D" in count:
        total += count["D"] * 15

    return total






