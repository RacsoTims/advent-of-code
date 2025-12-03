# URL:		https://adventofcode.com/2015/day/11
# Answer:	cqjxxyzz

import os
puzzle_input = '.\\day11_input.txt'
example_input = '.\\day11_example.txt'
if os.name == 'posix':
	puzzle_input = './day11_input.txt'
	example_input = './day11_example.txt'

puzzle_input = "cqjxjnds"
forbidden_chars = ["i", "l", "0"]
pairs = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff',
		'gg', 'hh', 'ii', 'jj', 'kk', 'll',
		'mm', 'nn', 'oo', 'pp', 'qq', 'rr',
		'ss', 'tt', 'uu', 'vv', 'ww', 'xx']
sequences = ['abc', 'bcd', 'cde', 'def', 'efg', 'fgh',
			'ghi', 'hij', 'ijk', 'jkl', 'klm', 'lmn',
			'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst',
			'stu', 'tuv', 'uvw', 'vwx', 'wxy', 'xyz']

def check_password(password) -> bool:
	valid = False
	if check_for_forbidden(password):
		if check_for_pairs(password):
			if check_for_sequence(password):
				valid = True
	return valid


def check_for_sequence(password) -> bool:
	check_passed = False
	for sequence in sequences:
		if sequence in password:
			check_passed = True
			break
	return check_passed


def check_for_forbidden(password) -> bool:
	check_passed = True
	for char in forbidden_chars:
		if char in password:
			check_passed = False
			break
	return check_passed


def check_for_pairs(password) -> bool:
	check_passed = False
	count = 0
	for pair in pairs:
		if pair in password:
			count += 1
		if count == 2:
			check_passed = True
			break
	return check_passed


if check_password(puzzle_input):
	print("The password is valid.")
else:
	print("The password is not valid.")
