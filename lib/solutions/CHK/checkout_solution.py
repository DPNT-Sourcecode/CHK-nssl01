

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
    while a > 0:
        if a >= 3:
            total += 130
            a -= 3
        else:
            total += 50
            a -= 1  

    return total




