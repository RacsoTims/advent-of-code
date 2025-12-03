# URL:		https://adventofcode.com/2023/day/1
# Answer:	57346

import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

sum_calibration_values = 0

with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		digits = [x for x in line if x.isdigit()]
		sum_calibration_values += int("".join([digits[0], digits[-1]]))
print(sum_calibration_values)
