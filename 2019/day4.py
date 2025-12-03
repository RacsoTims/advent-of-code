# URL:		https://adventofcode.com/2019/day/4
# Answer:	2090

import os
puzzle_input = '.\\day4_input.txt'
example_input = '.\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = './day4_input.txt'
	example_input = './day4_example.txt'

def check_candidate(n, digits):
	if check_adjacent(digits) and check_no_decrease(digits):
		return True
	else:
		return False


def check_adjacent(digits):
	adjacent = False
	for i in range(len(digits)):
		for j in range(i+1, len(digits)):
			if digits[i] == digits[j]:
				adjacent = True
				break
		if adjacent:
			break
	return adjacent


def check_no_decrease(digits):
	no_decrease = True
	for i in range(len(digits)):
		for j in range(i+1, len(digits)):
			if digits[i] > digits[j]:
				no_decrease = False
				break
		if not no_decrease:
			break
	return no_decrease


valid_passwords = 0
start = 130254
end = 678275

for n in range(start+1, end):
	digits = list(str(n))
	if check_candidate(n, digits):
		valid_passwords += 1
print(valid_passwords)
