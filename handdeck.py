import random
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
	def pop_card(self):
		return self.cards.pop()
	def add_card(self, card):
		self.cards.append(card)
	def shuffle(self):
		random.shuffle(self.cards)
	def move_cards(self, hand, num):
		for i in range(num):
			hand.add_card(self.pop_card())
        def m_sort(self):
                self.cards.sort(key=lambda x:x.suit)
	def deal_hands(self,nh,cph):
		ls=[]
		for i in range(nh):
			hand=Hand()
			for c in range(cph):
				hand.add_card(self.pop_card())
			ls.append(hand)
		return ls
class Hand(Deck):
	def __init__(self,label=''):
		self.cards=[]
		self.label=label

deck=Deck()
hand1=Hand()
print deck.deal_hands(3,4)
