# URL:	https://adventofcode.com/2024/day/5
# Answer:	0

import os
import re

path = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day5_input.txt'
if os.name == 'posix':
	path = '/home/oscar/projects/advent-of-code/2024/day5_input.txt'

pattern = r'(\d+)\|(\d+)'
count = 0
sum = 0
# pattern_pages = r'^\d+[,\d+]*$'

with open(path, "r") as puzzle_input:
    ordering_rules = []
    pages_to_produce = []
    for line in puzzle_input.readlines():
        if "|" in line:
            ordering_rules.append(re.findall(pattern, line)[0])
        elif "," in line:
            pages_to_produce.append(line.removesuffix("\n").split(","))

for pages in pages_to_produce[3:]:
    correct_order = True
    for rule in ordering_rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[1]) < pages.index(rule[0]):
                first = pages.index(rule[0])
                second = pages.index(rule[1])
                pages[second] = rule[0]
                pages[first] = rule[1]
                correct_order = False
    if not correct_order:
        sum += int(pages[(len(pages)//2)])
print(sum)
#                 correct_order = False
#                 break
#     if correct_order:
#         sum += int(pages[(len(pages)//2)])
# print(sum)
