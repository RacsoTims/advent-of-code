# URL:		https://adventofcode.com/2016/day/3#part2
# Answer:	1921

import numpy as np
import re
import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

count = 0
list_of_numbers = []

with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		numbers = [int(x) for x in re.findall("[0-9]+", line)]
		for n in numbers:
			list_of_numbers.append(n)

grid = np.array([list_of_numbers]).reshape(len(list_of_numbers) // 3, 3)

for i in range(grid.shape[1]):
    column = grid[:, i]
    for j in range(0,len(column),3):
        sides = column[j:j+3]
        sides.sort()
        if sum(sides[0:2]) > sides[-1]:
            count += 1
print(count)
