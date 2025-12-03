# URL:		https://adventofcode.com/2022/day/3
# Answer:	8085

import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

priority_lowercase = 1
priority_uppercase = 27
priority_sum = 0

shift_lowercase = ord('a') - priority_lowercase
shift_uppercase = ord('A') - priority_uppercase

with open(puzzle_input, 'r') as data:
	for rucksack in [x.removesuffix("\n") for x in data.readlines()]:
		common_type = "".join([y for y in rucksack[:len(rucksack)//2] if y in rucksack[len(rucksack)//2:]])[0]
		if common_type.islower():
			priority_sum += ord(common_type) - shift_lowercase
		else:
			priority_sum += ord(common_type) - shift_uppercase
print(priority_sum)
