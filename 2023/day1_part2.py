# URL:	https://adventofcode.com/2023/day/1#part2
# Answer:	0

import os
path = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day1_input.txt'
if os.name == 'posix':
	path = '/home/oscar/projects/advent-of-code/2023/day1_input.txt'

sum_calibration_values = 0
digits_spelled_out = {"one": '1', "two": '2', "three": '3',
					"four": '4', "five": '5', "six": '6',
					"seven": '7', "eight": '8', "nine": '9'}

with open(path, 'r') as puzzle_input:
	for line in puzzle_input.readlines():
		digits = ""
		i = 0
		j = 0
		while i < len(line):
			for j in range(i, len(line)):
				substring = line[i:j+1]
				if len(substring) == 1 and substring.isnumeric():
					digits += substring
					i += 1
					break
				elif substring in digits_spelled_out.keys():
					digits += digits_spelled_out[substring]
					i += 1
					break
				elif j == len(line) - 1:
					i += 1
		sum_calibration_values += int(digits[0] + digits[-1])

print(sum_calibration_values)
