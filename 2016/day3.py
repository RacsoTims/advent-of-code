# URL:		https://adventofcode.com/2016/day/3
# Answer:	1050

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day3_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2016/day3_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2016/day3_example.txt'

count = 0

with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		sides = [int(x) for x in re.findall("[0-9]+", line)]
		sides.sort()
		if sum(sides[0:2]) > sides[-1]:
			count += 1
print(count)
