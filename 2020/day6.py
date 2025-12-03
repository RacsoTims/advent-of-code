# URL:		https://adventofcode.com/2020/day/6
# Answer:	6775

import re
import os
puzzle_input = '.\\day6_input.txt'
example_input = '.\\day6_example.txt'
if os.name == 'posix':
	puzzle_input = './day6_input.txt'
	example_input = './day6_example.txt'

regex_empty = r'\n\s*\n'
count = 0

with open(puzzle_input, 'r') as data:
	for group in re.split(regex_empty, data.read()):
		count += len(set(group.replace("\n", "")))
print(count)
