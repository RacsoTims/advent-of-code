# URL:		https://adventofcode.com/2018/day/1
# Answer:	513

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2018\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2018\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2018/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2018/day1_example.txt'

frequency = 0

with open(puzzle_input, 'r') as data:
	for change in data.readlines():
		frequency += int(change)
print(frequency)
