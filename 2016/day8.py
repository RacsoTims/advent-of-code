# URL:		https://adventofcode.com/2016/day/8
# Answer:	123

import os
import numpy as np
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day8_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day8_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2016/day8_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2016/day8_example.txt'

def create_screen(pixels_tall, pixels_wide):
    return np.zeros((pixels_tall, pixels_wide),dtype=int)


def parse_instruction(instruction, screen):
    numbers = re.findall(r"\d+", instruction)
    if "rect" in instruction:   # instruction looks like "rect AxB" where A and B are numbers
        rows = int(numbers[1])
        columns = int(numbers[0])
        screen = light_up_rect(rows, columns, screen)
    if "rotate row" in instruction: # instruction looks like "rotate row y=A by B" where A and B are numbers
        row = int(numbers[0])
        shift = int(numbers[1])
        screen = rotate_row(row, shift, screen)
    if "rotate column" in instruction:  # instruction looks like "rotate column x=A by B" where A and B are numbers
        column = int(numbers[0])
        shift = int(numbers[1])
        screen = rotate_column(column, shift, screen)
    return screen


def light_up_rect(rows, columns, screen):
    screen[0:rows,0:columns] = 1
    return screen


def rotate_row(row, shift, screen):
    shifted_row = np.roll(screen[row], shift)
    screen[row] = shifted_row
    return screen


def rotate_column(column, shift, screen):
    shifted_column = np.roll(screen.T[column], shift)
    screen.T[column] = shifted_column
    return screen


pixels_tall = 6
pixels_wide = 50
screen = create_screen(pixels_tall, pixels_wide)

with open(puzzle_input, 'r') as data:
	instructions = [x.removesuffix("\n") for x in data.readlines()]

for instruction in instructions:
    screen = parse_instruction(instruction, screen)
# print(screen)
pixels_lit = int(np.sum(screen))
print(pixels_lit)
