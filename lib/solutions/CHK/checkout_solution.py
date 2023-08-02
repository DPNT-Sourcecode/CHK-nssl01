

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

valid = ["A", "B", "C", "D"]

def checkout(skus):
    # Anything but A, B, C, or D is invalid
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
    
    a = count["A"]
    # mod 3 * 130
    # a - (above * 3) * 50
    a_deals = (a // 3)
    total += a_deals * 130
    total += (a % 3) * 50

    b = count["B"]
    b_deals = (b // 2)
    total += b_deals * 45
    total += (b % 2) * 30



    return total






