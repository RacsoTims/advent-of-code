# URL:		https://adventofcode.com/2025/day/2
# Answer:	5398419778

import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

invalid_id_sum = 0

with open(puzzle_input, 'r') as data:
	for id_range in data.read().split(","):
		first_id = int(id_range.split("-")[0])
		last_id = int(id_range.split("-")[1])
		for id in range(first_id, last_id + 1):
			id = str(id)
			if len(id) % 2 == 0:
				invalid_id_sum += int(id) if id[:len(id)//2] == id[len(id)//2:] else 0
print(invalid_id_sum)
