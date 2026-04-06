# URL:		https://adventofcode.com/2015/day/16#part2
# Answer:	405

import os
import re

puzzle_input = '.\\day16_input.txt'
example_input = '.\\day16_example.txt'
if os.name == 'posix':
	puzzle_input = './day16_input.txt'
	example_input = './day16_example.txt'

machine = {"children": "exact", "cats": "greater than", "samoyeds": "exact",
		   "pomeranians": "fewer than", "akitas": "exact", "vizslas": "exact",
		   "goldfish": "fewer than", "trees": "greater than", "cars": "exact",
		   "perfumes": "exact"}

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
		matches = re.findall(regex_aunts, line)
		aunt_number = matches[0]
		aunt_is_sender = True

		for i in range(1, len(matches), 2):
			aunt_item = matches[i]
			aunt_quantity = matches[i + 1]
			calibration = machine[aunt_item]

			if calibration == "exact":
				if sender[aunt_item] != aunt_quantity:
					aunt_is_sender = False	
			elif calibration == "fewer than":
				if aunt_quantity >= sender[aunt_item]:
					aunt_is_sender = False	
			elif calibration == "greater than":
				if aunt_quantity <= sender[aunt_item]:
					aunt_is_sender = False
			if not aunt_is_sender:
				break

		if aunt_is_sender:
			print(aunt_number)
