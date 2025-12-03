# URL:		https://adventofcode.com/2017/day/2#part2
# Answer:	263

import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

checksum = 0

with open(puzzle_input, 'r') as data:
	for row in [list(map(int, (x.removesuffix("\n")).split("\t"))) for x in data.readlines()]:
		for i in range(len(row)):
			for j in range(i+1,len(row)):
				mod_ij = row[i] % row[j]
				mod_ji = row[j] % row[i]
				if mod_ij == 0:
					checksum += row[i] // row[j]
				elif mod_ji == 0:
					checksum += row[j] // row[i]
print(checksum)
