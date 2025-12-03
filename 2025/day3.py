# URL:		https://adventofcode.com/2025/day/3
# Answer:	0

import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

total_output = 0

with open(puzzle_input, 'r') as data:
	for bank in [l.removesuffix("\n") for l in data.readlines()]:
		batteries = list(bank)
		tens = max(batteries[:-1])
		tens_i = batteries.index(max(batteries[:-1]))
		joltage = int(tens + max(batteries[tens_i+1:]))
		total_output += joltage
print(total_output)
