# URL:		https://adventofcode.com/2018/day/3#part2
# Answer:	124

import numpy as np
import re
import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

dimensions = (1000, 1000)
grid = np.zeros((dimensions[0], dimensions[1]))

with open(puzzle_input, 'r') as data:
	instructions = data.readlines()

for instruction in instructions:
	numbers = list(map(int, re.findall(r'\d+', instruction)))
	grid[numbers[2]:numbers[2]+numbers[-1], numbers[1]:numbers[1]+numbers[-2]] += 1
for instruction in instructions:
	numbers = list(map(int, re.findall(r'\d+', instruction)))
	claim_id = numbers[0]
	claim_area = grid[numbers[2]:numbers[2]+numbers[-1], numbers[1]:numbers[1]+numbers[-2]]
	if np.all(claim_area == 1):
		break
print(claim_id)
