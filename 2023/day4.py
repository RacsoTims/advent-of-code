# URL:		https://adventofcode.com/2023/day/4
# Answer:	25571

import re
import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day4_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2023/day4_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2023/day4_example.txt'

total_score = 0

with open(puzzle_input, 'r') as data:
	for card in data.readlines():
		winning = re.findall(r'\d+', card[card.index(":"):card.index("|")+1])
		player_numbers = re.findall(r'\d+', card[card.index("|"):])
		matches = len([x for x in player_numbers if x in winning])
		total_score += int(2**(matches-1))
print(total_score)
