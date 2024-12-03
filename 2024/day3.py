# URL:              https://adventofcode.com/2024/day/3
# Correct answer:   183380722

import re

regex = r"mul\((\d{1,3}),(\d{1,3})\)"

with open("C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day3_input.txt", "r") as data:
    total = sum([int(x) * int(y) for x, y in re.findall(regex, data.read())])

print(total)
