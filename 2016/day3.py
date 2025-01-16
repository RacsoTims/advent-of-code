# URL: https://adventofcode.com/2016/day/3
# Answer:   1050

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day3_input.txt"
count = 0

with open(path, "r") as puzzle_input:
    for line in puzzle_input.readlines():
        sides = [int(x) for x in re.findall("[0-9]+", line)]
        sides.sort()
        if sum(sides[0:2]) > sides[-1]:
            count += 1
print(count)
