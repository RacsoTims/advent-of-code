# URL:              https://adventofcode.com/2024/day/4
# Correct answer:   ?

# 'Compass directions' used in this script:
# 'nse' from north to southeast
# 'wse' from west to southeast
# 'nsw' from north to southwest
# 'esw' from east to southwest

import numpy as np

def search_horizontally(grid, key) -> int:
    found = 0
    rows = grid.shape[0]
    for i in range(rows):
        forwards = "".join(grid[i]).count(key)
        backwards = "".join(grid[i][::-1]).count(key)
        found += forwards + backwards
    return found


def search_vertically(grid, key) -> int:
    found = 0
    columns = grid.shape[1]
    for i in range(columns):
        forwards = "".join(grid[:,i]).count(key)
        backwards = "".join(grid[:,i][::-1]).count(key)
        found += forwards + backwards
    return found


def search_diagonally(grid) -> int:
    found_total = 0
    rows, columns = grid.shape
    found_total += search_nse(rows, columns)
    found_total += search_wse(rows, columns)
    found_total += search_nsw(rows, columns)
    found_total += search_esw(rows, columns)
    return found_total


def search_nse(rows, columns):
    found = 0
    for column in range(columns):
        diagonal = ""
        row = 0
        while row < rows and column < columns:
            diagonal += grid[row, column]
            row += 1
            column += 1
        found += diagonal.count(key) + diagonal[::-1].count(key)
    return found


def search_wse(rows, columns):
    found = 0
    for row in range(1,rows):
        diagonal = ""
        column = 0
        while row < rows and column < columns:
            diagonal += grid[row, column]
            row += 1
            column += 1
        found += diagonal.count(key) + diagonal[::-1].count(key)
    return found


def search_nsw(rows, columns):
    found = 0
    for column in range(columns):
        diagonal = ""
        row = 0
        while row < rows and column >= 0:
            diagonal += grid[row, column]
            row += 1
            column -= 1
        found += diagonal.count(key) + diagonal[::-1].count(key)
    return found


def search_esw(rows,columns):
    found = 0
    for row in range(1,rows):
        diagonal = ""
        column = columns - 1
        while row < rows and column >= 0:
            diagonal += grid[row, column]
            row += 1
            column -= 1
        found += diagonal.count(key) + diagonal[::-1].count(key)
    return found


path = "/home/oscar/projects/advent-of-code/2024/day4_input.txt"
key = "XMAS"
total = 0

with open(path, "r") as data:
    lines = data.read().splitlines()

grid = np.array([list(line) for line in lines])

total += search_horizontally(grid, key)
total += search_vertically(grid, key)
total += search_diagonally(grid)
print(total)
