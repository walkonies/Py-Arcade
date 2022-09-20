from random import shuffle
cards = {
2 : '2',
3 : '3',
4 : '4',
5 : '5',
6 : '6',
7 : '7',
8 : '8',
9 : '9',
10 : '10',
11 : 'Jack',
12 : 'Queen',
13 : 'King',
14 : 'Ace'
}
suits= {
0 : 'Hearts',
1 : 'Clubs',
2 : 'Diamonds',
3 : 'Spades'
}
class Card:
	SUITS = suits
	CARDS = cards
	def __init__(self, card, suit):
		self.suit = suit
		self.val = card
		self.name = self.getName()
		self.color = 'red' if suit == 0 or suit == 2 else 'black'
	def getVal(self):
		return self.val
	def getName(self):
		return self.CARDS[self.val]
	def getSuit(self):
		return self.SUITS[self.suit]
	def __str__(self):
		return f'{self.name} of {self.getSuit()}'

class Deck:
	def __init__(self, size = 1):
		self.deck = []
		self.discard = []
		self.num_decks = size
		self.reset()
		self.size = self.getSize()
	def reset(self):
		self.setDeck(self.makeDeck(self.num_decks))
	def makeDeck(self, size):
		suits = Card.SUITS
		cards = Card.CARDS
		n_cards = len(cards)
		n_suits = len(suits)
		size *= 4
		deck = []
		for s in suits:
			for c in cards:
				deck.append(Card(c,s))

		return  deck
	def setDeck(self, deck):
		self.deck = deck
	def getDeck(self):
		return  self.deck
	def show(self):
		for card in self.getDeck():
			print(card)
	def shuffle(self):
		print('shuflling deck...')
		shuffle(self.deck)
	def isEmpty(self):
		return  self.getSize() == 0
	def getSize(self):
		return len(self.deck)
	def pop(self):
		card = None
		if not self.isEmpty():
			card = self.deck.pop()
			self.discard.append(card)
		return card
	def getNumCards(self,num):
		cards = []
		for i in range(num):
			if self.isEmpty():
				break
			cards.append(self.pop())
		return cards


def main():
	d = Deck()
	d.show()
	d.shuffle()
	while not d.isEmpty():
		print(d.pop())
if __name__ == '__main__':
	main()