import copy
from solutions.CHK.items import items
from solutions.CHK.shop import Group, Shop

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:
    if type(skus) != str:
        print("Wrong type")
        return -1

    # Anything non A-Z is invalid
    valid = items.keys()
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

    shop = Shop()
    for sku, amount in count.items():
        shop.add_item(sku, items[sku](amount))

    shop.add_effect("B", "E", 2)
    shop.add_effect("M", "N", 3)
    shop.add_effect("Q", "R", 3)

    shop.add_group(Group(["S", "T", "X", "Y", "Z"], 3, 45))

    return shop.get_total_price()
