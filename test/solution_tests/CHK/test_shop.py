from solutions.CHK import checkout_solution

class TestShop():
    def test_add_item(self):
        shop = checkout_solution.Shop()
        to_add = checkout_solution.Item(price = 50, amount = 2)
        shop.add_item("A", to_add)

        assert(len(shop.items) == 1)

        a = shop.items["A"]
        assert(a.price == 50)
        assert(a.amount == 2)

    