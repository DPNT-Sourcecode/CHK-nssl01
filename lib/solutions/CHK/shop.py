from dataclasses import dataclass
from typing import Dict, NewType, Type
from solutions.CHK.item import Item


SKU = NewType("SKU", str)


@dataclass
class Group:
    skus: [SKU]
    size: int
    price: int


class Shop:
    def __init__(self):
        self.items: Dict[SKU, Item] = {}
        self.effects = []
        self.groups = []

    def add_item(self, sku: SKU, item: Item):
        self.items[sku] = item

    def update_amount(self, sku: SKU, amount: int):
        self.items[sku].amount = amount

    def get_amount(self, sku: SKU):
        return self.items[sku].amount

    def get_total_price(self) -> int:
        """
        Gets total price of basket

        Cost affectors run in the following order:
        1. groups
        2. effects
        3. deals
        """
        total = self.run_groups()

        self.run_effects()
        for item in self.items.values():
            total += item.get_price()
        return total

    def add_group(self, group: Group):
        self.groups.append(group)

    def run_groups(self) -> int:
        """
        For each group, get as many groups as possible at the price given
        Removes the items and returns the price of all group deals
        """
        groups_total = 0
        seen = {}
        prev = []
        for group in self.groups:
            for sku in group.skus:
                if sku in self.items:
                    seen[sku] = self.items[sku].amount

            for sku, amount in seen.items():
                for _ in range(0, amount):
                    prev.append(sku)

                    if len(prev) == group.size:
                        groups_total += group.price
                        for sku in prev:
                            self.items[sku].amount -= 1

                        prev = []

        return groups_total

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





