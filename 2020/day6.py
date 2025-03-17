# URL:		https://adventofcode.com/2020/day/6
# Answer:	6775

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day6_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day6_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2020/day6_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2020/day6_example.txt'

regex_empty = r'\n\s*\n'
count = 0

with open(puzzle_input, 'r') as data:
	for group in re.split(regex_empty, data.read()):
		count += len(set(group.replace("\n", "")))
print(count)
