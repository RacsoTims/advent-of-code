# URL:		https://adventofcode.com/2019/day/2
# Answer:	4090689

import os
import math
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2019\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2019\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2019/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2019/day2_example.txt'

add = 1
multiply = 2
halt = 99

with open(puzzle_input, 'r') as data:
	program = [int(x) for x in data.read().split(",")]

current_position = 0
program[1] = 77
program[2] = 33

while program[current_position] != halt:
	integer = program[current_position]
	if integer == add:
		addends = [program[program[current_position+1]], program[program[current_position+2]]]
		program[program[current_position+3]] = sum(addends)
	elif integer == multiply:
		terms = [program[program[current_position+1]], program[program[current_position+2]]]
		program[program[current_position+3]] = math.prod(terms)
	current_position += 4
print(program)
