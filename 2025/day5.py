# URL:		https://adventofcode.com/2025/day/5
# Answer:	577

import re
import os
puzzle_input = '.\\day5_input.txt'
example_input = '.\\day5_example.txt'
if os.name == 'posix':
	puzzle_input = './day5_input.txt'
	example_input = './day5_example.txt'

fresh_ingredients = []
count = 0

with open(puzzle_input, 'r') as data:
	for line in [l for l in data.readlines() if l != "\n"]:
		if "-" in line:
			fresh_ingredients.append(list(map(int, re.findall(r'\d+', line))))
		else:
			for id_range in fresh_ingredients:
				if int(line) in range(id_range[0], id_range[1] + 1):
					count += 1
					break
print(count)
