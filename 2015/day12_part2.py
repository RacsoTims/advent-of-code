# URL:		https://adventofcode.com/2015/day/12#part2
# Answer:	0

import os
import re
puzzle_input = '.\\day12_input.txt'
example_input = '.\\day12_example.txt'
if os.name == 'posix':
	puzzle_input = './day12_input.txt'
	example_input = './day12_example.txt'

regex_general = r"\d+|-\d+"
regex_specific = r"{[^}]+red[^}]+}"

with open(puzzle_input, 'r') as data:
	content = data.read()

total = sum(map(int, re.findall(regex_general, content)))
faulty_matches = re.findall(regex_specific, content)
# print(total)

if len(faulty_matches) > 0:
	subtotal = 0
	for faulty in faulty_matches:
		subtotal += sum(map(int, re.findall(regex_general, faulty)))

total -= subtotal
print(total)
