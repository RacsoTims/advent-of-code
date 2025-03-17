# URL:		https://adventofcode.com/2020/day/2
# Answer:	640

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2020/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2020/day2_example.txt'

regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
valid = 0

with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		parts = re.match(regex, line)
		minimal_occurrences = int(parts[1])
		maximal_occurrences = int(parts[2])
		required_letter = parts[3]
		password = parts[4]
		if minimal_occurrences <= password.count(required_letter) <= maximal_occurrences:
			valid += 1
print(valid)
