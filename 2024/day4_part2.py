# URL:		https://adventofcode.com/2024/day/4#part2
# Answer:	1992

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day4_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2024/day4_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2024/day4_example.txt'

def search_pattern(grid):
    found = 0
    rows, columns = len(grid), len(grid[0])
    for r in range(1, rows-1):
        for c in range(1, columns-1):
            patterns = [(grid[r-1][c-1] == "M", grid[r][c] == "A", grid[r+1][c+1] == "S", grid[r-1][c+1] == "M", grid[r+1][c-1] == "S"),
                        (grid[r-1][c-1] == "M", grid[r][c] == "A", grid[r+1][c+1] == "S", grid[r-1][c+1] == "S", grid[r+1][c-1] == "M"),
                        (grid[r-1][c-1] == "S", grid[r][c] == "A", grid[r+1][c+1] == "M", grid[r-1][c+1] == "M", grid[r+1][c-1] == "S"),
                        (grid[r-1][c-1] == "S", grid[r][c] == "A", grid[r+1][c+1] == "M", grid[r-1][c+1] == "S", grid[r+1][c-1] == "M")]
            for pattern in patterns:
                if all(pattern):
                    found += 1
    return found


with open(puzzle_input, 'r') as data:
	grid = [list(x) for x in data.readlines()]
print(search_pattern(grid))
