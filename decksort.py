class Card(object):
   def __init__(self,s,r):
        suits= ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        ranks= [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
        self.suit=suits[s]
        self.rank=ranks[r]
        def __str__(self):
                return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
class Deck(object):
        def __init__(self):
                self.cards = []
                for suit in range(4):
                        for rank in range(1, 14):
                                card = Card(suit, rank)
                                self.cards.append(card)
        def __str__(self):
                res = []
                for card in self.cards:
                        res.append(str(card.suit+' of '+card.rank))
                return '\n'.join(res)
	def m_sort(self):
		self.cards.sort(key=lambda x:x.suit)

deck=Deck()
deck.m_sort()
print deck

