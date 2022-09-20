import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utilities.cards import Deck

def main():
	deck = Deck()
	deck.shuffle()

	num = input('How many young blood?\n')
	try:
		num = int(num)
	except Exception as e:
		num = 52

	num = 52 if num not in range(53) else num
	cards = deck.getNumCards(num)
	total = 0
	ace = False

	print(f'{"Card:":<18}Pushups:')
	for card in cards:
		val = card.val
		if val == 14:
			ace = not ace
			val = 15 if ace else 1
		print(f'{str(card):<18}{val}')
		total += val
		input()
	print(f'Total: {total}!!')
	
main()