# URL:		https://adventofcode.com/2020/day/5#part2
# Answer:	743

import numpy as np
import os
puzzle_input = '.\\day5_input.txt'
example_input = '.\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = './day5_input.txt'
	example_input = './day5_example.txt'

highest_id = 0
row_letters = 7
col_letters = 3
plane = np.zeros((128,8))

def calculate_row(partition):
	front = "F"
	remaining = [r for r in range(2**len(partition))]
	for letter in partition:
		if letter == front:
			remaining = remaining[:len(remaining)//2]
		else:
			remaining = remaining[len(remaining)//2:]
	row = int(remaining[0])
	return row


def calculate_col(partition):
	left = "L"
	remaining = [r for r in range(2**len(partition))]
	for letter in partition:
		if letter == left:
			remaining = remaining[:len(remaining)//2]
		else:
			remaining = remaining[len(remaining)//2:]
	column = int(remaining[0])
	return column


with open(puzzle_input, 'r') as data:
	for seat in [x.removesuffix("\n") for x in data.readlines()]:
		row_part = seat[:row_letters]
		col_part = seat[row_letters:row_letters+col_letters]
		
		row = calculate_row(row_part)
		col = calculate_col(col_part)
		seat_id = 8 * row + col
		plane[row][col] = 1
		
		if seat_id > highest_id:
			highest_id = seat_id

with open("day5_output.txt", 'w') as output:
	output.write(np.array2string(plane, threshold=np.inf))
