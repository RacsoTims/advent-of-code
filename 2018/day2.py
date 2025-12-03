# URL:		https://adventofcode.com/2018/day/2
# Answer:	6723

import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

two_occurrences = 0
three_occurrences = 0

with open(puzzle_input, 'r') as data:
	boxes = data.readlines()
	for box_ID in boxes:
		occurs_twice = False
		occurs_thrice = False
		for letter in box_ID:
			if box_ID.count(letter) == 2:
				occurs_twice = True
			elif box_ID.count(letter) == 3:
				occurs_thrice = True
		if occurs_twice:
			two_occurrences += 1
		if occurs_thrice:
			three_occurrences += 1

checksum = two_occurrences * three_occurrences
print(checksum)
