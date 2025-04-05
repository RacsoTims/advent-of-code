# URL:		https://adventofcode.com/2017/day/1
# Answer:	1144

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2017\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2017\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2017/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2017/day1_example.txt'

captcha_sum = 0

with open(puzzle_input, 'r') as data:
	sequence = data.read()
	for i in range(len(sequence)):
		digit = sequence[i]
		if digit == sequence[(i+1)%len(sequence)]:
			captcha_sum += int(digit)

print(captcha_sum)
