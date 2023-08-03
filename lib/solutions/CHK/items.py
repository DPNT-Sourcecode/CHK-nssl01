from solutions.CHK.item import Item, Price
from solutions.CHK.shop import SKU


# Takes 'Shop'
def e_effect(self) -> None:
    if "E" in self.items and "B" in self.items:
        b_amount = self.get_amount("B")
        e_amount = self.get_amount("E")
        b_amount_after_bogo = b_amount - (e_amount // 2)

        # No minus amounts
        self.items["B"].amount = max(0, b_amount_after_bogo)


# e_effect = make_effect()


# 3N get one M free
def n_effect(self) -> None:
    if "N" in self.items and "M" in self.items:
        affected_amount = self.get_amount("M")
        effect_amount = self.get_amount("N")
        amount_after_bogo = affected_amount - (effect_amount // 3)

        # No minus amounts
        self.items["M"].amount = max(0, amount_after_bogo)


# 3R get one Q free
def r_effect(self) -> None:
    if "R" in self.items and "Q" in self.items:
        affected_amount = self.get_amount("Q")
        effect_amount = self.get_amount("R")
        amount_after_bogo = affected_amount - (effect_amount // 3)

        # No minus amounts
        self.items["Q"].amount = max(0, amount_after_bogo)


items = {
    "A": lambda amount: Item([Price(1, 50), Price(3, 130), Price(5, 200)], amount),
    "B": lambda amount=0: Item([Price(1, 30), Price(2, 45)], amount),
    "C": lambda amount=0: Item(
        [
            Price(1, 20),
        ],
        amount,
    ),
    "D": lambda amount=0: Item([Price(1, 15)], amount),
    "E": lambda amount=0: Item([Price(1, 40)], amount),
    "F": lambda amount=0: Item([Price(1, 10), Price(2, 10)], amount),
    "G": lambda amount=0: Item([Price(1, 20)], amount),
    "H": lambda amount=0: Item([Price(1, 10), Price(5, 45), Price(10, 80)], amount),
    "I": lambda amount=0: Item([Price(1, 35)], amount),
    "J": lambda amount=0: Item([Price(1, 60)], amount),
    "K": lambda amount=0: Item([Price(1, 80), Price(2, 150)], amount),
    "L": lambda amount=0: Item([Price(1, 90)], amount),
    "M": lambda amount=0: Item([Price(1, 15)], amount),
    "N": lambda amount=0: Item([Price(1, 40)], amount, effect=n_effect),
    "O": lambda amount=0: Item([Price(1, 10)], amount),
    "P": lambda amount=0: Item([Price(1, 50), Price(5, 200)], amount),
    "Q": lambda amount=0: Item([Price(1, 30), Price(3, 80)], amount),
    "R": lambda amount=0: Item([Price(1, 50)], amount, effect=r_effect),
    "S": lambda amount=0: Item([Price(1, 30)], amount),
    "T": lambda amount=0: Item([Price(1, 20)], amount),
    "U": lambda amount=0: Item([Price(1, 40), Price(3, 80)], amount),
    "V": lambda amount=0: Item([Price(1, 50), Price(2, 90), Price(3, 130)], amount),
    "W": lambda amount=0: Item([Price(1, 20)], amount),
    "X": lambda amount=0: Item([Price(1, 90)], amount),
    "Y": lambda amount=0: Item([Price(1, 10)], amount),
    "Z": lambda amount=0: Item([Price(1, 50)], amount),
}




