# URL:		https://adventofcode.com/2017/day/6
# Answer:	4074

import os
puzzle_input = '.\\day6_input.txt'
example_input = '.\\day6_example.txt'
if os.name == 'posix':
	puzzle_input = './day6_input.txt'
	example_input = './day6_example.txt'

def find_bank_with_most_blocks(area) -> tuple:
	return (max(area), area.index(max(area)))


def distribute_blocks(area):
	blocks, bank = find_bank_with_most_blocks(area)
	current_bank = (bank+1) % len(area)
	for i in range(blocks, 0, -1):
		area[current_bank] += 1
		area[bank] -= 1
		current_bank = (current_bank+1) % len(area)
	return area


cycles = 0
configurations = []
no_repeat = True

with open(puzzle_input, 'r') as data:
	area = [int(x) for x in data.read().removesuffix("\n").split("\t")]
	configurations.append(area[:])

while no_repeat:
	new_configuration = distribute_blocks(area)
	if new_configuration in configurations:
		no_repeat = False
	else:
		configurations.append(new_configuration[:])
	cycles += 1
print(cycles)
