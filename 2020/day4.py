# URL:		https://adventofcode.com/2020/day/4
# Answer:	216

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day4_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2020/day4_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2020/day4_example.txt'

regex_chunks = r'\n\s*\n'
regex_pairs = r'\S+'

country_id = "cid"
valid = 0

with open(puzzle_input, 'r') as data:
	for chunk in re.split(regex_chunks, data.read()):
		passport = {}
		for pair in re.findall(regex_pairs, chunk):
			splt = pair.split(":")
			passport[splt[0]] = splt[1]
		if len(passport.keys()) == 8 or (len(passport.keys()) == 7 and country_id not in passport.keys()):
			valid += 1
print(valid)
