from typing import Dict, NewType, Type
from solutions.CHK.items import items
from solutions.CHK.checkout_solution import Item


SKU = NewType("SKU", str)

class Shop:
    def __init__(self):
        self.items: Dict[SKU, Item] = items

    def update_amount(self, sku: SKU, amount: int):
        self.items[sku].amount = amount

    def get_amount(self, sku: SKU):
        return self.items[sku].amount
    
    def get_total_price(self):
        self.run_effects()
        self.run_deals()
        return sum([x.price for x in self.items.values()])

    def add_item(self, sku: SKU, item: Type[Item]):
        self.items[sku] = item

    def run_effects(self):
        for item in self.items:
            if item.effect != None:
                item.effect()

    def run_deals(self):
        for item in self.items():
            if item.deal != None:
                item.deal()