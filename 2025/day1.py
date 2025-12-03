# URL:		https://adventofcode.com/2025/day/1
# Answer:	984

import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

turns = 100
dial = 50
count = 0

with open(puzzle_input, 'r') as data:
	for rotation in data.read().splitlines():
		distance = -(int(rotation[1:])) if "L" in rotation else int(rotation[1:])
		dial = (turns + dial + distance) % turns
		count += 1 if dial == 0 else 0
print(count)
