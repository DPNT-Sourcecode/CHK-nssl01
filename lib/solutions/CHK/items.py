from solutions.CHK.item import Item, Price
from solutions.CHK.shop import SKU


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
    "N": lambda amount=0: Item([Price(1, 40)], amount),
    "O": lambda amount=0: Item([Price(1, 10)], amount),
    "P": lambda amount=0: Item([Price(1, 50), Price(5, 200)], amount),
    "Q": lambda amount=0: Item([Price(1, 30), Price(3, 80)], amount),
    "R": lambda amount=0: Item([Price(1, 50)], amount),
    "S": lambda amount=0: Item([Price(1, 30)], amount),
    "T": lambda amount=0: Item([Price(1, 20)], amount),
    "U": lambda amount=0: Item([Price(1, 40), Price(3, 80)], amount),
    "V": lambda amount=0: Item([Price(1, 50), Price(2, 90), Price(3, 130)], amount),
    "W": lambda amount=0: Item([Price(1, 20)], amount),
    "X": lambda amount=0: Item([Price(1, 90)], amount),
    "Y": lambda amount=0: Item([Price(1, 10)], amount),
    "Z": lambda amount=0: Item([Price(1, 50)], amount),
}





