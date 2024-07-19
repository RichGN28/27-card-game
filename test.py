import button_functions as bf

deck = bf.create_27_cards_deck()

pile1, pile2, pile3 = bf.distribute(deck)

deck = bf.group_piles(pile1, pile2, pile3, 1, 0)
print(deck)