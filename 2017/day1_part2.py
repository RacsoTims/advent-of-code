# URL:		https://adventofcode.com/2017/day/1#part2
# Answer:	1194

import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

captcha_sum = 0

with open(puzzle_input, 'r') as data:
	sequence = data.read()
	length = len(sequence)
	for i in range(len(sequence)):
		digit = sequence[i]
		if digit == sequence[(i+length//2)%length]:
			captcha_sum += int(digit)

print(captcha_sum)
