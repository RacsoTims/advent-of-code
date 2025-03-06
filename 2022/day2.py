# URL:		https://adventofcode.com/2022/day/2
# Answer:	14375

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day2_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day2_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2022/day2_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2022/day2_example.txt'

rock = 1
paper = 2
scissors = 3

lose = 0
draw = 3
win = 6

table = {"AX": rock+draw, "AY": paper+win, "AZ": scissors+lose,
		"BX": rock+lose, "BY": paper+draw, "BZ": scissors+win,
		"CX": rock+win, "CY": paper+lose, "CZ": scissors+draw}

total_score = 0

with open(puzzle_input, 'r') as data:
	rounds = [x.removesuffix("\n").replace(" ", "") for x in data.readlines()]
	for round in rounds:
		total_score += table[round]
print(total_score)
