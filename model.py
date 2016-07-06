import random


class Card(object):
    """Represents a zet card.

    Attributes:
    Count: integer 0-3
    Color: integer 0-3
    Shape: integer 0-3
    Fill: integer 0-3
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
    """Represents a zet deck of 81 cards where each feature combination occurs precisely once in the deck."""

    def __init__(self):
        self.deck = []
        for count in range(3):
            for color in range(3):
                for shape in range(3):
                    for fill in range(3):
                        card = Card(count, color, shape, fill)
        self.deck.append(card)

    def shuffle(self):
        """Shuffles the cards in this deck."""

        random.shuffle(self.cards)

    def deal(self):
        """Deals 12 cards for Zet play."""

        self.deal = []
        for card in range(12):
            self.deal.append(card)


class Hand(x, y, z):
    """Represents a selection of 3 zet cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label

    def is_zet():
    """Determine if zet fulfills criteria of all the same OR all different on 4 criteria:  count, color, shape, fill)"""

        if not (x.count == y.count == z.count) | (x.count != y.count != z.count):
            return False

        if not (x.color == y.color == z.color) | (x.color != y.color != y.color):
            return False

        if not (x.shape == y.shape == z.shape) | (x.shape != y.shape != z.shape):
            return False

        if not (x.fill == y.fill == z.fill) | (x.fill != y.fill != z.fill):
            return False

        return True

        # if not (x[0] == y[0] == z[0]) | (x[0] != y[0] != z[0]):
        #     return False  # count

        # if not (x[1] == y[1] == z[1]) | (x[1] != y[1] != z[1]):
        #     return False  # color

        # if not (x[2] == y[2] == z[2]) | (x[2] != y[2] != z[2]):
        #     return False  # shape

        # if not (x[3] == y[3] == z[3]) | (x[3] != y[3] != z[3]):
        #     return False  # fill


if __name__ == "__main__":

    from server import app
