cards = [1, 6, 2, 5, 9, 4, 3]
cards_sorted = []

while cards:
    for i in cards:
        cards_sorted.append(cards.pop())

print(cards_sorted)
