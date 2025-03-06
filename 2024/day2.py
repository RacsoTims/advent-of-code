# URL:		https://adventofcode.com/2024/day/2
# Answer:	559

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2024/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2024/day2_example.txt'

count = 0

def check_safety(report) -> bool:
    safe = True
    increasing = report[::]
    decreasing = report[::]
    
    increasing.sort()
    decreasing.sort(reverse=True)
    
    if report == increasing or report == decreasing:
        for i in range(1, len(report)):
            diff = abs(report[i] - report[i-1])
            if diff < 1 or diff > 3:
                safe = False
    else:
        safe = False
    return safe


with open(puzzle_input, 'r') as data:
	lines = data.readlines()

for line in lines:
    report = list(map(int, line.split(" ")))
    if check_safety(report):
        count += 1
print(count)
