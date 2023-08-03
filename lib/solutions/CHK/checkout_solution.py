from solutions.CHK.items import items
from solutions.CHK.shop import Shop

# noinspection PyUnusedLocal
# skus = unicode string


        
def checkout(skus: str) -> int:
    if type(skus) != str:
        print("Wrong type")
        return -1
    
    # Anything but A, B, C, or D is invalid
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
    for sku, count in count:
        


    # a_total = ItemA(count.get("A", 0)).total_price()
    # c_total = ItemC(count.get("C", 0)).total_price()
    # d_total = ItemD(count.get("D", 0)).total_price()
    # e_total = ItemE(count.get("E", 0)).total_price()
    # f_total = ItemF(count.get("F", 0)).total_price()

    # b_count = count.get("B", 0)
    # # Remove the number we get free, which should be half the int div of E
    # # add on the remainders
    # if "E" in count and b_count != 0:
    #     b_amount_after_bogo = b_count - (count["E"] // 2)
    #     b_total = ItemB(b_amount_after_bogo).total_price()
    # else:
    #     b_total = ItemB(b_count).total_price()

    # print(a_total, b_total, c_total, d_total, e_total, f_total)
    # return a_total + b_total + c_total + d_total + e_total + f_total

    return 0

