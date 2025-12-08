# URL:		https://adventofcode.com/2025/day/4
# Answer:	0

import numpy
import os
puzzle_input = '.\\day4_input.txt'
example_input = '.\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = './day4_input.txt'
	example_input = './day4_example.txt'

def count_neighbours(coordinates, constraint) -> bool:
	accessible = True
	count = 0
	for row in range(-1, 2):
		for col in range(-1, 2):
			y = coordinates[0] + row
			x = coordinates[1] + col
			if not (-1 < x < 136) or not (-1 < y < 136):
				continue
			cell = grid[y][x]
			if cell == "@" and not (row == 0 and col == 0):
				count += 1
			if count >= constraint:
				accessible = False
				break
	return accessible

grid = numpy.zeros((136, 136), dtype=str)
constraint = 4
access = 0

with open(puzzle_input, 'r') as data:
	lines = [l.removesuffix("\n") for l in data.readlines()]
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			grid[i][j] = lines[i][j]

for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == ".":
			continue
		elif count_neighbours([i, j], constraint):
			access += 1
print(access)
