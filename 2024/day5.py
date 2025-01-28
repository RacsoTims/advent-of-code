# URL:              https://adventofcode.com/2024/day/5
# Correct answer:   ?

import re

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day5_input.txt"
pattern = r'(\d+)\|(\d+)'
count = 0
# pattern_pages = r'^\d+[,\d+]*$'

with open(path, "r") as puzzle_input:
    ordering_rules = []
    pages = []
    for line in puzzle_input.readlines():
        if "|" in line:
            ordering_rules.append(re.findall(pattern, line)[0])
        elif "," in line:
            pages.append(line.removesuffix("\n").split(","))
# print(ordering_rules)
# print(pages)
for update in pages:
    correct_order = True
    for page_number in update:
        pass
    if correct_order:
        print(update)
