# URL:		https://adventofcode.com/2023/day/2#part2
# Answer:	65371

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2023/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2023/day2_example.txt'

sum_powers = 0

with open(puzzle_input, 'r') as data:
	for game in data.readlines():
		game_ID = int(re.match(r'Game (\d+)', game)[1])
		reds = list(map(int, re.findall(r'(\d+) red', game)))
		greens = list(map(int, re.findall(r'(\d+) green', game)))
		blues = list(map(int, re.findall(r'(\d+) blue', game)))
		sum_powers += max(reds) * max(greens) * max(blues)
print(sum_powers)
