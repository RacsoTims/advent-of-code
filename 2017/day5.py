# URL:		https://adventofcode.com/2017/day/5
# Answer:	351282

import os
puzzle_input = '.\\day5_input.txt'
example_input = '.\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = './day5_input.txt'
	example_input = './day5_example.txt'

steps = 0

with open(puzzle_input, 'r') as data:
	instructions = [int(x.removesuffix("\n")) for x in data.readlines()]
	current_position = 0
	new_position = 0
	while current_position < len(instructions):
		new_position += instructions[current_position]
		instructions[current_position] += 1
		steps += 1
		current_position = new_position
print(steps)
