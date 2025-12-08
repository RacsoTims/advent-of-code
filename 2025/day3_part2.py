# URL:		https://adventofcode.com/2025/day/3#part2
# Answer:	168794698570517

import os
puzzle_input = '.\\day3_input.txt'
example_input = '.\\day3_example.txt'
if os.name == 'posix':
	puzzle_input = './day3_input.txt'
	example_input = './day3_example.txt'

total_output = 0

with open(puzzle_input, 'r') as data:
	for line in [l.removesuffix("\n") for l in data.readlines()]:
		turn_on = 12
		cursor = 0
		bank = list(map(int, list(line)))
		batteries = [0 for j in range(turn_on)]
		for i in range(len(batteries)):
			section = bank[cursor:len(bank) - turn_on + 1]
			largest = max(section)
			largest_i = section.index(largest)
			batteries[i] = largest
			turn_on -= 1
			if largest_i == 0:
				cursor += 1
			else:
				cursor += largest_i + 1
		total_output += int("".join(map(str, batteries)))
print(total_output)
