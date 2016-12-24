from Card import Card
from random import shuffle

class Deck(object):

    def __init__(self):
        # list of 52 cards, with 1 of each rank and suite
        self.cards = []

        for i in xrange(1,14):
            new_card = Card("S", i)
            self.cards.append(new_card)

        for i in xrange(1,14):
            new_card = Card("C", i)
            self.cards.append(new_card)

        for i in xrange(1,14):
            new_card = Card("D", i)
            self.cards.append(new_card)

        for i in xrange(1,14):
            new_card = Card("H", i)
            self.cards.append(new_card)

        shuffle(self.cards)

    def draw_card(self):
        card = self.cards[0]
        del self.cards[0]
        return card
