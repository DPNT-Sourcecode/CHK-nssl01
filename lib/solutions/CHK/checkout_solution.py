

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


