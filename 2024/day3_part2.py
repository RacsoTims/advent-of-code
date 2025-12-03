# URL:		https://adventofcode.com/2024/day/3#part2
# Answer:	82733683

import re
import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
pattern_extended = r'(?<=\))'
total = 0
enabled = True

with open(puzzle_input, 'r') as data:
	valid = re.split(pattern_extended, data.read())

for instruction in valid:
    if "don't()" in instruction:
        enabled = False
    elif "do()" in instruction:
        enabled = True
    else:
        match = re.search(pattern, instruction)
        if match and enabled:
            x, y = map(int, match.groups())
            total += x*y
print(total)
