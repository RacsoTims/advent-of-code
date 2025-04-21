# URL:		https://adventofcode.com/2023/day/1#part2
# Answer:	57345

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2023/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2023/day1_example.txt'

digits_map = {"one": "1", "two": "2", "three": "3",
		"four": "4", "five": "5", "six": "6",
		"seven": "7", "eight": "8", "nine": "9"}
sum_calibration_values = 0

def extract_digits(line) -> list:
	digits = []
	for i in range(len(line)):
		if line[i].isdigit():
			digits.append(line[i])
		else:
			for k in digits_map.keys():
				if line[i:i+len(k)] == k:
					digits.append(digits_map[k])
	return digits


with open(puzzle_input, 'r') as data:
	for line in data.readlines():
		digits = extract_digits(line)
		sum_calibration_values += int("".join([digits[0], digits[-1]]))
print(sum_calibration_values)
