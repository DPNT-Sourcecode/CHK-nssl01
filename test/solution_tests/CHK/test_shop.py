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
            1: 50,
            2: 100,
            # 3 for 130
            3: 130,
            # 3 for 130 + 1 for 50
            4: 180,
            # 5 for 200
            5: 200,
            # 8 for 200 + 3 for 130
            8: 330
        }

        for amount, price in expected.items():
            items["A"].amount = amount
            assert(items["A"].total_price() == price)


    # 2E get one B free
    def test_e_effect(self):
        shop = Shop()
        
