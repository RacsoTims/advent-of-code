# URL:		https://adventofcode.com/2025/day/1#part2
# Answer:	5657

from math import floor
import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

turns = 100
dial = 50
count = 0

with open(puzzle_input, 'r') as data:
	for rotation in data.read().splitlines():
		distance = -(int(rotation[1:])) if "L" in rotation else int(rotation[1:])
		complete_turns = floor(abs(distance) / (turns+1)) if dial == 0 else floor(abs(distance) / turns)
		passed_zero = 0 if 0 <= dial + (distance % turns) <= turns or dial == 0 else 1
		dial = (turns + dial + distance) % turns
		count += complete_turns + passed_zero + 1 if dial == 0 else complete_turns + passed_zero
print(count)
