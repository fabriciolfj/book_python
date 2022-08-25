from Vector import Vector
from french_deck import Card, FrenchDeck


beer_card = Card('7', 'diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))


v1 = Vector(2, 4)
v2 = Vector(2, 1)
v3 = v1 + v2
print(v3)

v4 = v1 * 3
print(v4)
print(abs(v1))
print(bool(v1))
v5 = abs(4)
print(v5)