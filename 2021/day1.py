# URL:		https://adventofcode.com/2021/day/1
# Answer:	1624

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2021/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2021/day1_example.txt'

count = 0

with open(puzzle_input, 'r') as data:
	measurements = data.readlines()
	for i in range(1, len(measurements)):
		if int(measurements[i]) > int(measurements[i-1]):
			count += 1

print(count)
