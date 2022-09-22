import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utilities.cards import Deck
from utilities.utilities import log, readCSV, getDate

directory = os.path.join(os.getcwd(),os.path.dirname(__file__))
log_path = os.path.join(directory,'data','pushup_log.csv')

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
		ex = input()
		if ex == 'q':
			break

	print(f'Total: {total}!!')

		       # Data, Cards, Pushpus
	data = f'{getDate()},{num},{total}'
	log(log_path, data)
	
if __name__ == '__main__':
	main()