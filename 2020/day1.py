# URL:		https://adventofcode.com/2020/day/1
# Answer:	1018944

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2020/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2020/day1_example.txt'

number = 2020
found = False

with open(puzzle_input, 'r') as data:
	report = [int(x) for x in data.readlines()]
	for i in range(len(report)-1):
		for j in range(i+1, len(report)):
			if report[i] + report[j] == number:
				print(report[i] * report[j])
				found = True
		if found:
			break
