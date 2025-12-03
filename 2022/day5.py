# URL:		https://adventofcode.com/2022/day/5
# Answer:	VQZNJMWTR

import re
import os
puzzle_input = '.\\day5_input.txt'
example_input = '.\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = './day5_input.txt'
	example_input = './day5_example.txt'

message = ""
stacks = {'1': ['R', 'H', 'M', 'P', 'Z'],
		'2': ['B', 'J', 'C', 'P'],
		'3': ['D', 'C', 'L', 'G', 'H', 'N', 'S'],
		'4': ['L', 'R', 'S', 'Q', 'D', 'M', 'T', 'F'],
		'5': ['M', 'Z', 'T', 'B', 'Q', 'P', 'S', 'F'],
		'6': ['G', 'B', 'Z', 'S', 'F', 'T'],
		'7': ['V', 'R', 'N'],
		'8': ['M', 'C', 'V', 'D', 'T', 'L', 'G', 'P'],
		'9': ['L', 'M', 'F', 'J', 'N', 'Q', 'W']}

with open(puzzle_input, 'r') as data:
	for instruction in data.readlines():
		if "move" in instruction:
			numbers = re.findall(r'\d+', instruction)
			boxes_to_move = numbers[0]
			stack_from = numbers[1]
			stack_to = numbers[2]
			for i in range(int(boxes_to_move)):
				stacks[stack_to].insert(0, stacks[stack_from][0])
				stacks[stack_from].pop(0)

for stack in stacks.values():
	message += stack[0]
print(message)
