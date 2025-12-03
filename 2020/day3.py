# URL:		https://adventofcode.com/2020/day/3
# Answer:	237

import numpy as np
import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

slope = (3, 1)
current_position = (0,0)
tree_sign = "#"
trees_encountered = 0

def create_grid(rows):
	number_of_rows = len(rows)
	row_size = len(rows[0])
	grid = np.zeros((number_of_rows, row_size),dtype=str)
	for i in range(len(rows)):
		for j in range(len(rows[i])):
			grid[i][j] = rows[i][j]
	return grid


with open(puzzle_input, 'r') as data:
	rows = [x.removesuffix("\n") for x in data.readlines()]

grid = create_grid(rows)
for k in range(len(rows) - 1):
	current_position = (current_position[0]+slope[0], current_position[1]+slope[1])
	try:
		if str(grid[current_position[1]][current_position[0]]) == tree_sign:
			trees_encountered += 1
	except(IndexError):
		row_size = len(rows[0])
		if str(grid[current_position[1]][((current_position[0]+1)%row_size)-1]) == tree_sign:
			trees_encountered += 1
print(trees_encountered)
