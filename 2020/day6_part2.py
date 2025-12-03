# URL:		https://adventofcode.com/2020/day/6#part2
# Answer:	3356

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
		group_size = group.count("\n") + 1
		if group_size == 1:
			count += len(group)
		else:
			group = group.replace("\n", "")
			answers = set(group)
			for letter in answers:
				if group.count(letter) == group_size:
					count += 1
print(count)
