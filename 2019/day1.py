# URL:		https://adventofcode.com/2019/day/1
# Answer:	3563458

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2019\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2019\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2019/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2019/day1_example.txt'

total_fuel = 0

with open(puzzle_input, 'r') as data:
	for mass in [int(x) for x in data.readlines()]:
		total_fuel += mass // 3 - 2
print(total_fuel)
