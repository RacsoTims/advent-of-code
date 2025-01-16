# URL: https://adventofcode.com/2016/day/2#part2
# Answer:   A7AC3

import numpy as np

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day2_input.txt"
grid = np.array([["", "", "1", "", ""],
                ["", "2", "3", "4", ""],
                ["5", "6", "7", "8", "9"],
                ["", "A", "B", "C", ""],
                ["", "", "D", "", ""]])
row = 2
column = 0
code = ""

def execute_step(step, row, column):
    if step == "U":
        row = up(row)
    if step == "D":
        row = down(row)
    if step == "L":
        column = left(column)
    if step == "R":
        column = right(column)
    return row, column


def up(row):
    if row != 0 and grid[row-1][column] != "":
        row -= 1
    return row


def down(row):
    if row != len(grid) - 1 and grid[row+1][column] != "":
        row += 1
    return row


def left(column):
    if column != 0 and grid[row][column-1] != "":
        column -= 1
    return column


def right(column):
    if column != len(grid) - 1 and grid[row][column+1] != "":
        column += 1
    return column


with open(path, "r") as puzzle_input:
    for line in puzzle_input.readlines():
        for step in line.removesuffix("\n"):
            row, column = execute_step(step, row, column)
            position = grid[row][column]
        code += str(position)
print(code)
