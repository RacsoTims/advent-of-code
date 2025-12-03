# URL:		https://adventofcode.com/2017/day/4
# Answer:	325

import os
puzzle_input = '.\\day4_input.txt'
example_input = '.\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = './day4_input.txt'
	example_input = './day4_example.txt'

valid = 0

with open(puzzle_input, 'r') as data:
	for passphrase in [x.removesuffix("\n").split(" ") for x in data.readlines()]:
		for word in passphrase:
			if passphrase.count(word) > 1:
				break
			elif word == passphrase[-1]:
				valid += 1
print(valid)
