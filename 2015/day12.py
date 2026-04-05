# URL:		https://adventofcode.com/2015/day/12
# Answer:	156366

import os
import re

puzzle_input = '.\\day12_input.txt'
example_input = '.\\day12_example.txt'
if os.name == 'posix':
	puzzle_input = './day12_input.txt'
	example_input = './day12_example.txt'

regex = r"\d+|-\d+"

with open(puzzle_input, 'r') as data:
	content = data.read()

print(sum(map(int, re.findall(regex, content))))
