# URL:		https://adventofcode.com/2017/day/5#part2
# Answer:	24568703

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
		offset = instructions[current_position]
		new_position += offset
		if offset >= 3:
			instructions[current_position] -= 1
		else:
			instructions[current_position] += 1
		steps += 1
		current_position = new_position
print(steps)
