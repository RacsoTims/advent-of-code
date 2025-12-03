# URL:		https://adventofcode.com/2020/day/2#part2
# Answer:	472

import re
import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
valid = 0

with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		parts = re.match(regex, line)
		first = int(parts[1])
		second = int(parts[2])
		required_letter = parts[3]
		password = parts[4]
		if (password[first-1] == required_letter) != (password[second-1] == required_letter):
			valid += 1
print(valid)
