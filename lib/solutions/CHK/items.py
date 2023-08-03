from solutions.CHK.item import Item

def a_deal(self: Item) -> int:
    amount = self.amount
    total = 0

    a_5_deals = amount // 5
    total += a_5_deals * 200
    amount -= a_5_deals * 5

    a_3_deals = (amount // 3)
    total += a_3_deals * 130
    amount -= a_3_deals * 3

    total += amount * self.price

    return total

def b_deal(self: Item) -> int:
        amount = self.amount
        total = 0

        b_deals = (amount // 2)
        total += b_deals * 45
        total += (amount % 2) * self.price

        return total

def f_deal(self: Item) -> int:
        n_to_remove = self.amount // 3
        amount = self.amount - n_to_remove
        
        return amount * self.price

# Takes 'Shop'
def e_effect(self) -> None:
    if self.items["E"] != 0 and "B" in self.items:
        b_amount = self.get_amount("B")
        e_amount = self.get_amount("E")
        b_amount_after_bogo = b_amount - (e_amount // 2)

        # No minus amounts
        self.items["B"].amount = max(0, b_amount_after_bogo)


items = {
    "A": lambda amount = 0: Item(50, amount=amount, deal=a_deal),
    "B": lambda amount = 0: Item(30, amount=amount, deal=b_deal),
    "C": lambda amount = 0: Item(20, amount=amount),
    "D": lambda amount = 0: Item(15, amount=amount),
    "E": lambda amount = 0: Item(40, amount=amount, effect=e_effect),
    "F": lambda amount = 0: Item(10, amount=amount, deal=f_deal),
    "G": lambda amount = 0: Item(20, amount=amount),
    "H": lambda amount = 0: Item(10, amount=amount),
    "I": lambda amount = 0: Item(35, amount=amount),
    "J": lambda amount = 0: Item(60, amount=amount),
    "K": lambda amount = 0: Item(80, amount=amount),
    "L": lambda amount = 0: Item(90, amount=amount),
    "M": lambda amount = 0: Item(15, amount=amount),
    "N": lambda amount = 0: Item(40, amount=amount),
    "O": lambda amount = 0: Item(10, amount=amount),
    "P": lambda amount = 0: Item(50, amount=amount),
    "Q": lambda amount = 0: Item(30, amount=amount),
    "R": lambda amount = 0: Item(50, amount=amount),
    "S": lambda amount = 0: Item(30, amount=amount),
    "T": lambda amount = 0: Item(20, amount=amount),
    "U": lambda amount = 0: Item(40, amount=amount),
    "V": lambda amount = 0: Item(50, amount=amount),
    "W": lambda amount = 0: Item(20, amount=amount),
    "X": lambda amount = 0: Item(90, amount=amount),
    "Y": lambda amount = 0: Item(10, amount=amount),
    "Z": lambda amount = 0: Item(50, amount=amount)
}
