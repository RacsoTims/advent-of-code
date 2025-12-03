# URL:		https://adventofcode.com/2024/day/5
# Answer:	5329

import re
import os
puzzle_input = '.\\day5_input.txt'
example_input = '.\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = './day5_input.txt'
	example_input = './day5_example.txt'

pattern = r'(\d+)\|(\d+)'
count = 0
sum = 0

with open(puzzle_input, 'r') as data:
	ordering_rules = []
	pages_to_produce = []
	for line in data.readlines():
		if "|" in line:
			ordering_rules.append(re.findall(pattern, line)[0])
		elif "," in line:
			pages_to_produce.append(line.removesuffix("\n").split(","))

for pages in pages_to_produce:
    correct_order = True
    for rule in ordering_rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[1]) < pages.index(rule[0]):
                # first = pages.index(rule[0])
                # second = pages.index(rule[1])
                # pages[second] = rule[0]
                # pages[first] = rule[1]
                correct_order = False
    if correct_order:
        sum += int(pages[(len(pages)//2)])
print(sum)
