# URL:      https://adventofcode.com/2021/day/1
# Answer:   1624

path = "/home/oscar/projects/advent-of-code/2021/day1_input.txt"
count = 0

with open(path, 'r') as puzzle_input:
    measurements = puzzle_input.readlines()
    for i in range(1, len(measurements)):
        if int(measurements[i]) > int(measurements[i-1]):
            count += 1

print(count)
