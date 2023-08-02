from solutions.CHK import Shop, Item

class TestShop():
    def test_add_item(self):
        shop = Shop()
        to_add = Item("A", 50)
        shop.add_item()