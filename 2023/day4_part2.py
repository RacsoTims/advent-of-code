# URL:		https://adventofcode.com/2023/day/4#part2
# Answer:	8805731

import re
import os
puzzle_input = '.\\day4_input.txt'
example_input = '.\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = './day4_input.txt'
	example_input = './day4_example.txt'

matches_per_card = {}
scratch_cards = {}

with open(puzzle_input, 'r') as data:
	cards = data.readlines()

for i in range(len(cards)):
	card = cards[i]
	winning_numbers = re.findall(r'\d+', card[card.index(":"):card.index("|")+1])
	player_numbers = re.findall(r'\d+', card[card.index("|"):])
	matches = len([x for x in player_numbers if x in winning_numbers])
	matches_per_card[f"card {i}"] = matches
	scratch_cards[f"card {i}"] = 1

for j in range(len(scratch_cards.values())):
	copies = list(scratch_cards.values())[j]
	if copies == 0:
		continue
	else:
		while copies > 0:
			for k in range(j+1, j+1+list(matches_per_card.values())[j]):
				if k == len(cards):
					break
				else:
					scratch_cards[f"card {k}"] += 1
			copies -= 1

cards_won = sum(scratch_cards.values())
print(cards_won)
