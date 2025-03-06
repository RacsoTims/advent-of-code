# URL:		https://adventofcode.com/2015/day/2#part2
# Answer:	3737498

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
    dimensions.pop(dimensions.index(max(dimensions)))   # remove longest side
    ribbon_wrap = 2*sum(dimensions)
    ribbon_bow = l*w*h
    total += ribbon_wrap + ribbon_bow
print(total)
