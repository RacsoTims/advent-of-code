# URL:		https://adventofcode.com/2016/day/2#part2
# Answer:	76792

import os
import numpy as np
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2016/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2016/day2_example.txt'

grid = np.arange(1, 10).reshape(3, 3)
row = 1
column = 1
code = ""

def execute_step(step, row, column):
    if step == "U":
        row = up(row)
    if step == "D":
        row = down(row)
    if step == "L":
        column = left(column)
    if step == "R":
        column = right(column)
    return row, column


def up(row):
    if row != 0:
        row -= 1
    return row


def down(row):
    if row != len(grid) - 1:
        row += 1
    return row


def left(column):
    if column != 0:
        column -= 1
    return column


def right(column):
    if column != len(grid) - 1:
        column += 1
    return column


with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		for step in line.removesuffix("\n"):
			row, column = execute_step(step, row, column)
			position = grid[row][column]
		code += str(position)
print(code)
