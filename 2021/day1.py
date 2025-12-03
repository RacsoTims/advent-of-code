# URL:		https://adventofcode.com/2021/day/1
# Answer:	1624

import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

count = 0

with open(puzzle_input, 'r') as data:
	measurements = data.readlines()
	for i in range(1, len(measurements)):
		if int(measurements[i]) > int(measurements[i-1]):
			count += 1
print(count)
