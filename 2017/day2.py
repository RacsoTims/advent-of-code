# URL:		https://adventofcode.com/2017/day/2
# Answer:	37923

import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

checksum = 0

with open(puzzle_input, 'r') as data:
	for row in [list(map(int, (x.removesuffix("\n")).split("\t"))) for x in data.readlines()]:
		checksum += max(row) - min(row)
print(checksum)
