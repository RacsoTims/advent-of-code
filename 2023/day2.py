# URL:		https://adventofcode.com/2023/day/2
# Answer:	3059

import re
import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

max_red = 12
max_green = 13
max_blue = 14
sum_IDs = 0

with open(puzzle_input, 'r') as data:
	for game in data.readlines():
		game_ID = int(re.match(r'Game (\d+)', game)[1])
		reds = list(map(int, re.findall(r'(\d+) red', game)))
		greens = list(map(int, re.findall(r'(\d+) green', game)))
		blues = list(map(int, re.findall(r'(\d+) blue', game)))
		if max(reds) <= max_red and max(greens) <= max_green and max(blues) <= max_blue:
			sum_IDs += game_ID
print(sum_IDs)
