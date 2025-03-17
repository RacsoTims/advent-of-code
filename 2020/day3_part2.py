# URL:		https://adventofcode.com/2020/day/3#part2
# Answer:	2106818610

import os
import numpy as np
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day3_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2020/day3_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2020/day3_example.txt'

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
tree_sign = "#"
product = 1

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
for slope in slopes:
	current_position = (0,0)
	trees_encountered = 0
	right = slope[0]
	down = slope[1]
	for k in range(0, len(rows) - 1, down):
		current_position = (current_position[0]+right, current_position[1]+down)
		try:
			if str(grid[current_position[1]][current_position[0]]) == tree_sign:
				trees_encountered += 1
		except(IndexError):
			row_size = len(rows[0])
			if str(grid[current_position[1]][((current_position[0]+1)%row_size)-1]) == tree_sign:
				trees_encountered += 1
	product *= trees_encountered
print(product)
