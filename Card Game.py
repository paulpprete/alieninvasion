#Blackjack game!
from random import choice

Ace = 11
Jack = 10
King = Queen = Jack
Card = [Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King]
Suit = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
def game():
	reset = input('Would you like to play a game of blackjack? ')
	while reset == 'yes' or 'Yes':
		x = choice(Card)
		y = choice(Card)
		i = x + y
		print(f'Your first card is the {x} of {random.choice(Suit)} and your second card is the {y} of {random.choice(Suit)}') 
		print(f'Your total is {i}')
		while i < 21:
			draw = input('If you would like to draw another card, please type yes.')
			if draw == 'yes' or 'Yes':
				z = choice(Card)
				i += z
				if x or y or z == Ace:
					if i > 21:
						Ace = 1
				elif i > 21:
					print('Sorry! Better luck next time!')
				else:
					print('Blackjack!')
		if i == 21:
			print('Blackjack!')
game()