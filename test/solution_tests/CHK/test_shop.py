from solutions.CHK.checkout_solution import Item, Shop
from solutions.CHK.items import items

class TestShop():
    def test_add_item(self):
        shop = Shop()
        to_add = Item(price = 50, amount = 2)
        shop.add_item("A", to_add)

        assert(len(shop.items) == 1)

        a = shop.items["A"]
        assert(a.price == 50)
        assert(a.amount == 2)

    def test_a_deal(self):
        items["A"].amount = 1
        assert(items["A"].deal()

    
