# URL:		https://adventofcode.com/2015/day/3
# Answer:	2592

import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

locations_visited = []
position_santa= [0,0]       # Santa's position on the grid given as coordinates (X, Y)
locations_visited.append(position_santa)

def move(position, direction) -> list:
    new_position = position[:]
    if direction == "^":
        new_position[1] += 1
    elif direction == "v":
        new_position[1] -= 1
    elif direction == ">":
        new_position[0] += 1
    else:
        new_position[0] -= 1
    return new_position


def check_if_visited(position) -> bool:
    visited_before = position in locations_visited
    return visited_before


with open(puzzle_input, 'r') as data:
	directions = data.read()

for direction in directions:
    position_santa = move(position_santa, direction)
    if not check_if_visited(position_santa):
        locations_visited.append(position_santa)
print(len(locations_visited))
