# URL:              https://adventofcode.com/2024/day/3#part2
# Correct answer:   183380722

import re

regex = r"mul\((\d{1,3}),(\d{1,3})\)"
regex_extended = r"(?<=\))"

with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day3_input.txt", "r") as data:
    valid = re.split(regex_extended, data.read())

total = 0
enabled = True
for instruction in valid:
    if "don't()" in instruction:
        enabled = False
    elif "do()" in instruction:
        enabled = True
    else:
        match = re.search(regex, instruction)
        if match and enabled:
            x, y = map(int, match.groups())
            total += x*y

print(total)
