# URL:		https://adventofcode.com/2015/day/16
# Answer:	103

import os
import re

puzzle_input = '.\\day16_input.txt'
example_input = '.\\day16_example.txt'
if os.name == 'posix':
	puzzle_input = './day16_input.txt'
	example_input = './day16_example.txt'

regex_sender = r"^(\w+)\:\s(\d+)"
regex_aunts = r"\d+|(?<=\s)\w+"
sender = {}

with open(example_input, 'r') as data:
	for line in data.read().split("\n"):
		matches = re.match(regex_sender, line)
		item_sender = matches[1]
		quantity_sender = matches[2]
		sender[item_sender] = quantity_sender

# print(sender)

with open(puzzle_input, "r") as data:
	for line in data.read().split("\n"):
		aunt_is_sender = True
		matches = re.findall(regex_aunts, line)
		aunt_number = matches[0]
		for i in range(1, len(matches), 2):
			aunt_item = matches[i]
			aunt_quantity = matches[i + 1]
			if sender[aunt_item] != aunt_quantity:
				aunt_is_sender = False
				break
		if aunt_is_sender:
			print(aunt_number)
