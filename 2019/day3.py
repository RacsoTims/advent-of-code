# URL:		https://adventofcode.com/2019/day/3
# Answer:	0

import os
import numpy as np
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2019\\day3_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2019\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2019/day3_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2019/day3_example.txt'

def draw_wire_path(instructions):
	for instruction in instructions:
		pass


def find_closest_intersection():
	pass


grid = np.zeros((10,11))

with open(example_input, 'r') as data:
	for instructions in data.readlines():
		draw_wire_path(instructions)

minimal_distance = find_closest_intersection()
print(minimal_distance)
