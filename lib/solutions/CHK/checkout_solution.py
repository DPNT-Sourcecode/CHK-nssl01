

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

def checkout(skus):
    total = 0
    for sku in skus:
        if sku in prices:
            total += prices[sku]

    return total


