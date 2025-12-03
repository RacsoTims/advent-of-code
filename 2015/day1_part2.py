# URL:		https://adventofcode.com/2015/day/1#part2
# Answer:	1795

import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

floor = 0

with open(puzzle_input, 'r') as data:
	directions = data.read()
	for i in range(len(directions)):
		if directions[i] == "(":
			floor += 1
		else:
			floor -= 1
		if floor == -1:
			print(i+1)
			break
