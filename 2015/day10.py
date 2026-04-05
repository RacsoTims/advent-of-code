# URL:		https://adventofcode.com/2015/day/10
# Answer:	252594

import os
puzzle_input = '.\\day10_input.txt'
example_input = '.\\day10_example.txt'
if os.name == 'posix':
	puzzle_input = './day10_input.txt'
	example_input = './day10_example.txt'

rounds = 40

with open(puzzle_input, 'r') as data:
	string_of_digits = data.read()
# print(string_of_digits)

def calculate_next_string(string_of_digits):
	next_string = ""
	current_digit = string_of_digits[0]
	count = 1
	for i in range(1, len(string_of_digits)):
		if string_of_digits[i] == current_digit:
			count += 1
		else:
			next_string += str(count) + current_digit
			current_digit = string_of_digits[i]
			count = 1
	next_string += str(count) + current_digit
	return next_string


while rounds:
	string_of_digits = calculate_next_string(string_of_digits)
	# print(string_of_digits)
	rounds -= 1

print(len(string_of_digits))
