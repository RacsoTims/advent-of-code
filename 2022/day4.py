# URL:		https://adventofcode.com/2022/day/4
# Answer:	305

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day4_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2022/day4_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2022/day4_example.txt'

pattern = r'(\d+)-(\d+),(\d+)-(\d+)'
count = 0

with open(puzzle_input, 'r') as data:
	pairs = [list(map(int, x)) for x in re.findall(pattern, data.read())]
	for pair in pairs:
		if (pair[0] <= pair[2] and pair[1] >= pair[3]) or (pair[2] <= pair[0] and pair[3] >= pair[1]) :
			count += 1
print(count)
