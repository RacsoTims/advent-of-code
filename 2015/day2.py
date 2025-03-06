# URL:		https://adventofcode.com/2015/day/2
# Answer:	1586300

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2015\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2015/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2015/day2_example.txt'

total = 0

with open(puzzle_input, 'r') as data:
	boxes = [n.removesuffix("\n").split("x") for n in data.readlines()]

for box in boxes:
    dimensions = [int(x) for x in box]
    l = dimensions[0]
    w = dimensions[1]
    h = dimensions[2]
    surface_area = [2*l*w, 2*w*h, 2*h*l]
    slack = min(surface_area) // 2
    total += sum(surface_area) + slack
print(total)
