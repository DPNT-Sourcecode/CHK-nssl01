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
        expected = {
            "A": 50,
            "AA": 100,
            # 3 for 130
            "AAA": 130,
            # 3 for 130 + 1 for 50
            "AAAA": 180,
            # 5 for 200
            "AAAAA": 200,
            # 8 for 200 + 3 for 130
            "AAAAAAAA": 330
        }


        items["A"].amount = 1
        assert(items["A"].total_price() == 50)

        items["A"].amount = 3
        assert(items["A"].total_price() == 130)

        items["A"].amount = 5
        assert(items["A"].total_price() == 200)
    