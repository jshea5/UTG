import random

value_mapping = {11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}
value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suit_mapping = {1: 'Clubs', 2: 'Spades', 3: 'Diamonds', 4: 'Hearts'}
suit = ['Clubs', 'Spades', 'Diamonds', 'Hearts']

card1_value = random.choice(value)
card1_suit = random.choice(suit)
card1 = f'{value_mapping.get(card1_value, card1_value)} of {card1_suit}'

card2_value = random.choice(value)
card2_suit = random.choice(suit)
while card2_value == card1_value and card2_suit == card1_suit:
    card2_value = random.choice(value)
    card2_suit = random.choice(suit)
card2 = f'{value_mapping.get(card2_value, card2_value)} of {card2_suit}'

print(card1)
print(card2)

if card1_value == card2_value and card1_value >= 5:
    paired = 1
else:
    paired = 0

if card1_suit == card2_suit:
    suited = 1
else:
    suited = 0

if suited == 1 and card1_value + card2_value > 20:
    big = 1
else:
    big = 0

if paired == 1 or big == 1:
    in_range = 1
else:
    in_range = 0

if in_range == 1:
    choice = input('Check or Bet: ')
    if choice == 'bet':
        print('Correct!')
    elif choice == 'check':
        print('Incorrect')
    else:
        print("Invalid Choice, try again.")
else:
    choice = input('Check or Bet: ')
    if choice == 'bet':
        print('Incorrect')
    elif choice == 'check':
        print('Correct!')
    else:
        print("Invalid Choice, try again.")

























