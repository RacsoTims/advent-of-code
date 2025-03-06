# URL:		https://adventofcode.com/2015/day/1
# Answer:	74

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2015/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2015/day1_example.txt'

with open(puzzle_input, 'r') as data:
	directions = data.read()
	floor = directions.count("(") - directions.count(")")
print(floor)
