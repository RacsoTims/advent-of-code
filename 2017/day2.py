# URL:		https://adventofcode.com/2017/day/2
# Answer:	37923

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2017\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2017\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2017/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2017/day2_example.txt'

checksum = 0

with open(puzzle_input, 'r') as data:
	for row in [list(map(int, (x.removesuffix("\n")).split("\t"))) for x in data.readlines()]:
		checksum += max(row) - min(row)
print(checksum)
