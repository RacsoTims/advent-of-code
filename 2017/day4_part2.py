# URL:		https://adventofcode.com/2017/day/4#part2
# Answer:	119

import os
puzzle_input = '.\\day4_input.txt'
example_input = '.\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = './day4_input.txt'
	example_input = './day4_example.txt'

valid = 0

with open(puzzle_input, 'r') as data:
	for passphrase in [x.removesuffix("\n").split(" ") for x in data.readlines()]:
		for i in range(len(passphrase)):
			letters = list(passphrase[i])
			letters.sort()
			passphrase[i] = "".join(letters)
			word = passphrase[i]
			if passphrase.count(word) > 1:
				break
			elif word == passphrase[-1]:
				valid += 1
print(valid)
