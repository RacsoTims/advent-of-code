# URL:		https://adventofcode.com/2015/day/6
# Answer:	377891

import os
import numpy as np
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day6_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day6_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2015/day6_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2015/day6_example.txt'

grid = np.zeros((1000,1000))

with open(puzzle_input, 'r') as data:
	raw = [x.removesuffix("\n") for x in data.readlines()]

for instruction in raw:
    action = re.split("[0-9]", instruction, 1)[0].removesuffix(" ")
    key = "[0-9]+"
    coordinates = re.findall(key, instruction)
    
    row_start = int(coordinates[0])
    row_end = int(coordinates[2])
    col_start = int(coordinates[1])
    col_end = int(coordinates[3])
    subgrid = grid[row_start:row_end+1,col_start:col_end+1]
    
    if action == "turn on":
        subgrid.fill(1)
    elif action == "turn off":
        subgrid.fill(0)
    else:
        on = np.where(subgrid == 1)
        off = np.where(subgrid == 0)
        for light in list(zip(*on)):
            subgrid[light[0]][light[1]] = 0
        for dark in list(zip(*off)):
            subgrid[dark[0]][dark[1]] = 1
print(int(np.sum(grid)))
