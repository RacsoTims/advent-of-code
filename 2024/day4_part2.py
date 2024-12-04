# URL:              
# Correct answer:   

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


path = "/home/oscar/projects/advent-of-code/2024/day4_input.txt"

with open(path, "r") as data:
    grid = [list(x) for x in data.read().splitlines()]

print(search_pattern(grid))
