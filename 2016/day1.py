# URL:		https://adventofcode.com/2016/day/1
# Answer:	332

import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

def calculate_distance(instructions):
    x, y = 0, 0     # Santa's position represented as X and Y coordinates
    direction_index = 0  # North (0), East (1), South (2), West (3)
    directions_order = ["N", "E", "S", "W"]
    
    move_vector = {
        'N': (0, 1),
        'E': (1, 0),
        'S': (0, -1),
        'W': (-1, 0)}
    
    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])
        
        if turn == 'L':
            direction_index = (direction_index - 1) % 4
        elif turn == 'R':
            direction_index = (direction_index + 1) % 4
        
        current_direction = directions_order[direction_index]
        dx, dy = move_vector[current_direction]
        
        x += dx * steps
        y += dy * steps
    
    return abs(x) + abs(y)


with open(puzzle_input, 'r') as data:
	instructions = data.read().split(", ")
shortest_distance = calculate_distance(instructions)
print(shortest_distance)
