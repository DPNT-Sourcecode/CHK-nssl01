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

# maybe ill come back to this when required..

# class Checkout:
#     def __init__(self, skus) -> None:
#         self.skus = skus

#         count = {}
#         for sku in skus:
#             if sku in count:
#                 count[sku] += 1
#             else:
#                 count[sku] = 1

#         self.counts = count

#     def get_count(self, sku: str) -> int:
#         if sku in self.counts:
#             return self.counts[sku]
#         else:
#             return 0



# class Item:
#     def __init__(self, price, amount, deal: Optional[callable] = None) -> None:
#         self.price: int = price
#         self.amount: int = amount
#         self.deal: callable = deal

#     def get_price(self):
#         if self.deal != None:
#             return self.deal()
#         else:
#             return self.price * self.amount    


def checkout(skus: str) -> int:
    if type(skus) != str:
        return -1
    
    # Anything but A, B, C, or D is invalid
    valid = prices.keys()
    for sku in skus:
        if sku not in valid:
            return -1
        
    count = {}

    for sku in skus:
        if sku in count:
            count[sku] += 1
        else:
            count[sku] = 1

    total = 0


    
    if "A" in count:
        a = count["A"]
        a_5_deals = a // 5
        total += a_5_deals * 200
        a -= a_5_deals 
        print(a)

        a_3_deals = (a // 3)
        total += a_3_deals * 130
        a -= a_3_deals
        print(a)

        total += a * prices["A"]

    if "B" in count:
        b = count["B"]
        b_deals = (b // 2)
        total += b_deals * 45
        total += (b % 2) * prices["B"]

    if "C" in count:
        total += count["C"] * prices["C"]

    if "D" in count:
        total += count["D"] * prices["D"]

    if "E" in count:
        e = count["E"]
        e_bogo = (e // 2)
        total -= e_bogo * 1
        total += (e % 2) * prices["E"]

    return total


