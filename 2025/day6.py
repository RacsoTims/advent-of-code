# URL:		https://adventofcode.com/2025/day/6
# Answer:	0

import re
import math
import os
puzzle_input = '.\\day6_input.txt'
example_input = '.\\day6_example.txt'
if os.name == 'posix':
	puzzle_input = './day6_input.txt'
	example_input = './day6_example.txt'

grand_total = 0

with open(puzzle_input, 'r') as data:
	lines = [l.removesuffix("\n").strip() for l in data.readlines()]
	first_terms = re.split(r"\s+", lines[0])
	for i in range(len(first_terms)):
		terms = [first_terms[i]]
		for j in range(1, len(lines)):
			terms.append(re.split(r"\s+", lines[j])[i])
		if "+" in terms:
			grand_total += sum(map(int, terms[:-1]))
		else:
			grand_total += math.prod(map(int, terms[:-1]))
print(grand_total)
