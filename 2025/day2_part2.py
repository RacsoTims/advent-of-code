# URL:		https://adventofcode.com/2025/day/2#part2
# Answer:	15704845910

from sympy import isprime
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
			length = len(id)
			if isprime(len(id)):
				invalid_id_sum += int(id) if id == length * id[0] else 0
			else:
				for divisor in [n for n in range(1, length) if length % n == 0]:
					if id == length//divisor * id[:divisor]:
						invalid_id_sum += int(id)
						break
print(invalid_id_sum)
