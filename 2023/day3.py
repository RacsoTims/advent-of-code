# URL:		https://adventofcode.com/2023/day/3
# Answer:	551094

import numpy as np
import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

sum_parts = 0

def check_submatrix(i,j, grid) -> bool:
	result = False
	directions = [(-1, -1), (-1, 0), (-1, 1), (0,-1), (0,1), (1, -1), (1, 0), (1,1)]
	for x,y in directions:
		try:
			cell = grid[i+x][j+y]
			if not cell.isdigit() and cell != ".":
				result = True
		except(IndexError):
			continue
	return result


with open(puzzle_input, 'r') as data:
	lines = [x.removesuffix("\n") for x in data.readlines()]

grid = np.array([list(line) for line in lines])
numbers = []

for i in range(len(grid)):
	number = []
	status = []
	for j in range(len(grid[i])):
		if grid[i][j].isdigit():
			number.append(grid[i][j])
			status.append(check_submatrix(i, j, grid))
		else:
			if len(number) > 0 and True in status:
				numbers.append(number)
			number = []
			status = []

print(sum([int("".join(x)) for x in numbers]))
