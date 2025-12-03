# URL:		https://adventofcode.com/2015/day/8
# Answer:	0

import re
import os
puzzle_input = '.\\day8_input.txt'
example_input = '.\\day8_example.txt'
if os.name == 'posix':
	puzzle_input = './day8_input.txt'
	example_input = './day8_example.txt'

hex = r'\\x[a-f0-9]{2}'
escaped_quote = r'(?<=.)"(?=.)'

string_literals_total = 0
in_memory_total = 0

with open(puzzle_input, 'r') as data:
	text = data.read()
	for line in text.split("\n"):
		string_literals_total += len(line)
		print(line)
		in_memory_total += len(line) - len("\"\"") - len(re.findall(escaped_quote, line)) - len(re.findall(r'\\', line)) - 3 * len(re.findall(hex, line))
print(string_literals_total)
print(in_memory_total)
print(string_literals_total - in_memory_total)
