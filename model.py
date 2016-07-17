import random


class Card(object):
    """Represents a zet card.

    Attributes:
    Count: integer 0-3
    Color: integer 0-3
    Shape: integer 0-3
    Fill: integer 0-3

    Example: 
    [0, 1, 2, 2] is a card that has these attributes:
    ['1', 'Blue', 'bone', 'speckle']
    """

    count_names = ['1','2','3']
    color_names = ['Red', 'Blue', 'Green']
    shape_names = ['circle', 'square', 'bone']
    fill_names = ['solid', 'empty', 'speckle']

    def __init__(self, count, color, shape, fill):
        self.count = count
        self.color = color
        self.shape = shape
        self.fill = fill

    def __repr__(self):
        """Provide helpful representation when printed, for human readability."""

        return "<Card count=%s color=%s shape=%s fill=%s>" % (self.count, 
            self.color, self.shape, self.fill)



class Deck(object):
    """Represents a zet deck of 81 cards where each feature combination occurs precisely once in the deck.

    Example:
    [
        [0,1,2,2],
        [1,2,0,1],
        [0,0,0,0], . . . ]

        0 <= i <= 3   is the number of columns (of 4 attributes)
        0 <= j <= 80  is the number of rows (of 81 cards)
    """

    def __init__(self):
        self.cards = []
        for count in range(3):
            for color in range(3):
                for shape in range(3):
                    for fill in range(3):
                        card = Card(count, color, shape, fill)
                        self.cards.append(card)

    def shuffle(self):
        """Shuffles cards in the deck."""

        random.shuffle(self.cards)

    def newDeal(self):
        """ Deals 12 cards for Zet play.

        Example:
        [
            [0,1,2,2],
            [1,2,0,1],
            [0,0,0,0], . . . ]

        0 <= i <= 3   is the number of columns (of 4 attributes)
        0 <= j <= 11  is the number of rows (of 12 cards)
        """

        deal_cards = []

        for i,card in range(13):
            deal_cards.append(self.cards.pop(i))

        return deal_cards


    def findZets(self):
        """Identify all the zets in a newDeal."""

        found = []

        for i, card_i in enumerate(self.deal):
            for j, card_j in enumerate(self.deal[i+1:], i+1):
                for k, card_k in enumerate(self.cards[j+1:], j+1):
                    if card_i.is_zet(card_j, card_k):
                        found.append((card_i, card_j, card_k))
        return found


    def is_zet(x, y,z):
        """Determine if a selection of 3 cards fulfills criteria of all the same OR all different on 4 criteria:  count, color, shape, fill)."""

        if not (x.count == y.count == z.count) | (x.count != y.count != z.count):
            return False

        if not (x.color == y.color == z.color) | (x.color != y.color != y.color):
            return False

        if not (x.shape == y.shape == z.shape) | (x.shape != y.shape != z.shape):
            return False

        if not (x.fill == y.fill == z.fill) | (x.fill != y.fill != z.fill):
            return False

        return True


if __name__ == "__main__":

    from server import app
