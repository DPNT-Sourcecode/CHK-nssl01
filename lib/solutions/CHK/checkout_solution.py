from solutions.CHK.items import items
from solutions.CHK.shop import Shop

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
        shop.update_amount(sku, amount)

    shop.run_effects()
    shop.run_deals()

    return shop.get_total_price()


