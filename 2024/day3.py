# URL:		https://adventofcode.com/2024/day/3
# Answer:	183380722

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day3_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2024/day3_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2024/day3_example.txt'

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

with open(puzzle_input, 'r') as data:
	total = sum([int(x) * int(y) for x, y in re.findall(pattern, data.read())])
print(total)
