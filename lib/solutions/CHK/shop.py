from typing import Dict, NewType, Type
from solutions.CHK.item import Item


SKU = NewType("SKU", str)


class Shop:
    def __init__(self):
        self.items: Dict[SKU, Item] = {}

    def add_item(self, sku: SKU, item: Item):
        self.items[sku] = item

    def update_amount(self, sku: SKU, amount: int):
        self.items[sku].amount = amount

    def get_amount(self, sku: SKU):
        return self.items[sku].amount

    def get_total_price(self):
        self.run_effects()
        total = 0
        for sku, item in self.items.items():
            total += item.get_price()
        return total

    def add_effect(self, affected: SKU, cause: SKU, amount: int):
        if affected in self.items and cause in self.items:
            affected_amount = self.get_amount(affected)
            effect_amount = self.get_amount(cause)
            amount_after_bogo = affected_amount - (effect_amount // 3)

            # No minus amounts
            self.items[affected].amount = max(0, amount_after_bogo)

    def run_effects(self):
        for item in self.items.values():
            if item.effect != None:
                item.effect(self)


