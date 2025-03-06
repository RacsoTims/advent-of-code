# URL:		https://adventofcode.com/2022/day/3#part2
# Answer:	2515

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day3_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2022/day3_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2022/day3_example.txt'

priority_lowercase = 1
priority_uppercase = 27
priority_sum = 0

shift_lowercase = ord('a') - priority_lowercase
shift_uppercase = ord('A') - priority_uppercase

with open(puzzle_input, 'r') as data:
	rucksacks = [x.removesuffix("\n") for x in data.readlines()]
	for i in range(0, len(rucksacks), 3):
		badge = "".join([y for y in rucksacks[i] if y in rucksacks[i+1] and y in rucksacks[i+2]])[0]
		if badge.islower():
			priority_sum += ord(badge) - shift_lowercase
		else:
			priority_sum += ord(badge) - shift_uppercase

print(priority_sum)
