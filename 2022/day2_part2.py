# URL:		https://adventofcode.com/2022/day/2#part2
# Answer:	10274

import os
puzzle_input = '.\\day2_input.txt'
example_input = '.\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = './day2_input.txt'
	example_input = './day2_example.txt'

rock = 1
paper = 2
scissors = 3

lose = 0
draw = 3
win = 6

table = {"AX": scissors+lose, "AY": rock+draw, "AZ": paper+win,
		"BX": rock+lose, "BY": paper+draw, "BZ": scissors+win,
		"CX": paper+lose, "CY": scissors+draw, "CZ": rock+win}

total_score = 0

with open(puzzle_input, 'r') as data:
	rounds = [x.removesuffix("\n").replace(" ", "") for x in data.readlines()]
	for round in rounds:
		total_score += table[round]
print(total_score)
