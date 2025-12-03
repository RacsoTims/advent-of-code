# URL:		https://adventofcode.com/2016/day/3
# Answer:	1050

import re
import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

count = 0

with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		sides = [int(x) for x in re.findall("[0-9]+", line)]
		sides.sort()
		if sum(sides[0:2]) > sides[-1]:
			count += 1
print(count)
