# URL:		https://adventofcode.com/2020/day/4#part2
# Answer:	150

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day4_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2020/day4_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2020/day4_example.txt'

regex_chunks = r'\n\s*\n'
regex_pairs = r'\S+'

country_id = "cid"
valid_passports = 0

def check_passport_validity(passport):
	if not check_missing(passport):
		return False
	if not check_byr(passport):
		return False
	if not check_iyr(passport):
		return False
	if not check_eyr(passport):
		return False
	if not check_hgt(passport):
		return False
	if not check_hcl(passport):
		return False
	if not check_ecl(passport):
		return False
	if not check_pid(passport):
		return False
	return True


def check_missing(passport):
	fields = passport.keys()
	if len(fields) == 8 or (len(fields) == 7 and country_id not in fields):
		return True
	else:
		return False


def check_byr(passport):
	min = 1920
	max = 2002
	birth_year = passport['byr']
	
	if birth_year.isnumeric():
		if min <= int(birth_year) <= max:
			return True
		else:
			False
	else:
		return False


def check_iyr(passport):
	min = 2010
	max = 2020
	issue_year = passport['iyr']
	
	if issue_year.isnumeric():
		if min <= int(issue_year) <= max:
			return True
		else:
			False
	else:
		return False


def check_eyr(passport):
	min = 2020
	max = 2030
	expiration_year = passport['eyr']
	
	if expiration_year.isnumeric():
		if min <= int(expiration_year) <= max:
			return True
		else:
			False
	else:
		return False


def check_hgt(passport):
	min_cm = 150
	max_cm = 193
	min_inch = 59
	max_inch = 76
	
	regex = r'^(\d+)[a-z]{2}$'
	height = passport['hgt']
	
	if re.fullmatch(regex, height) != None:
		value = int(re.search(r'\d+', height).group(0))
		unit = re.search(r'[a-z]{2}', height).group(0)
		if unit == "cm" and (min_cm <= value <= max_cm):
			return True
		elif unit == "in" and (min_inch <= value <= max_inch):
			return True
		else:
			return False
	else:
		return False


def check_hcl(passport):
	regex = r'^\#[a-f|0-9]{6}$'
	hair_colour = passport['hcl']
	
	if re.fullmatch(regex, hair_colour) != None:
		return True
	else:
		return False


def check_ecl(passport):
	eye_colour = passport['ecl']
	colours = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	if eye_colour in colours:
		return True
	else:
		return False


def check_pid(passport):
	passport_id = passport['pid']
	regex = r'^[0-9]{9}$'
	if re.fullmatch(regex, passport_id) != None:
		return True
	else:
		return False


with open(puzzle_input, 'r') as data:
	for chunk in re.split(regex_chunks, data.read()):
		passport = {}
		for pair in re.findall(regex_pairs, chunk):
			splt = pair.split(":")
			passport[splt[0]] = splt[1]
		if check_passport_validity(passport):
			valid_passports += 1
print(valid_passports)
