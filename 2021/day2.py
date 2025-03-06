# URL:		https://adventofcode.com/2021/day/2
# Answer:	1488669

import os
import math
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2021/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2021/day2_example.txt'

current_position = [0, 0]

def move(instruction, current_position):
    magnitude = int(instruction.split(" ")[1])
    if "forward" in instruction:
        current_position[0] += magnitude
    elif "down" in instruction:
        current_position[1] += magnitude
    else:
        current_position[1] -= magnitude
    return current_position


with open(puzzle_input, 'r') as data:
	instructions = data.readlines()
	for instruction in instructions:
		current_position = move(instruction, current_position)

print(math.prod(current_position))
