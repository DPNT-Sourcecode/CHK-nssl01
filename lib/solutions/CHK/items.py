from solutions.CHK.checkout_solution import Item

def a_deal(self) -> int:
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

def e_effect(self) -> None:
    if "E" in count and b_count != 0:
        b_amount_after_bogo = b_count - (count["E"] // 2)
        b_total = ItemB(b_amount_after_bogo).total_price()
    else:
        b_total = ItemB(b_count).total_price()

items = {
    "A": Item(50, deal=a_deal),
    "B": Item(30),
    "C": Item(20),
    "D": Item(15),
    "E": Item(40),
    "F": Item(10),
    "G": Item(20),
    "H": Item(10),
    "I": Item(35),
    "J": Item(60),
    "K": Item(80),
    "L": Item(90),
    "M": Item(15),
    "N": Item(40),
    "O": Item(10),
    "P": Item(50),
    "Q": Item(30),
    "R": Item(50),
    "S": Item(30),
    "T": Item(20),
    "U": Item(40),
    "V": Item(50),
    "W": Item(20),
    "X": Item(90),
    "Y": Item(10),
    "Z": Item(50)
}