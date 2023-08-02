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


    
    if "A" in count:
        a = count["A"]

        a_5_deals = a // 5
        total += a_5_deals * 200
        a -= a_5_deals * 5

        a_3_deals = (a // 3)
        total += a_3_deals * 130
        a -= a_3_deals * 3

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

        # we only want to make as many Bs free as we have 
        if "B" in count:
            if count["B"] < e_bogo:
                total -= count["B"] * prices["B"]
            else:
                total -= e_bogo * prices["B"]

        total += count["E"] * prices["E"]

    return total






