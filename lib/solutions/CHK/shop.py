from typing import Dict, NewType, Type
from solutions.CHK.item import Item


SKU = NewType("SKU", str)


class Shop:
    def __init__(self):
        self.items: Dict[SKU, Item] = {}
        self.effects = []

    def add_item(self, sku: SKU, item: Item):
        self.items[sku] = item

    def update_amount(self, sku: SKU, amount: int):
        self.items[sku].amount = amount

    def get_amount(self, sku: SKU):
        return self.items[sku].amount

    def get_total_price(self):
        self.run_effects()
        total = 0
        for item in self.items.values():
            total += item.get_price()
        return total

    def add_group(self, skus: [SKU], group_size: int, price: int):
        count = 0
        

    def add_effect(self, affected: SKU, cause: SKU, amount: int):
        """
        Add an effect that will cause an amount of one SKU to impact another
        affected: The SKU of the item impacted by the effect
        cause: The SKU of the item that causes the effect
        amount: The amount of cause required to have the effect
        """

        def effect():
            if affected in self.items and cause in self.items:
                affected_amount = self.get_amount(affected)
                effect_amount = self.get_amount(cause)
                amount_after_bogo = affected_amount - (effect_amount // amount)

                # No minus amounts
                self.items[affected].amount = max(0, amount_after_bogo)

        self.effects.append(effect)

    def run_effects(self):
        for effect in self.effects:
            effect()

