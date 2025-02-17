# URL:      https://adventofcode.com/2021/day/2#part2
# Answer:   1176514794

import math

path = "/home/oscar/projects/advent-of-code/2021/day2_input.txt"
current_position = [0, 0, 0]    # horizontal position, depth, aim

def move(instruction, current_position):
    magnitude = int(instruction.split(" ")[1])
    if "forward" in instruction:
        current_position[0] += magnitude
        current_position[1] += current_position[2] * magnitude
    elif "down" in instruction:
        current_position[2] += magnitude
    else:
        current_position[2] -= magnitude
    return current_position


with open(path, 'r') as puzzle_input:
    instructions = puzzle_input.readlines()
    for instruction in instructions:
        current_position = move(instruction, current_position)

print(math.prod(current_position[0:2]))
