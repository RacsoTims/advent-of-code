# URL:	https://adventofcode.com/2023/day/1
# Answer:	0

import os
path = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2023\\day1_input.txt'
if os.name == 'posix':
	path = '/home/oscar/projects/advent-of-code/2023/day1_input.txt'

sum_calibration_values = 0
with open(path, 'r') as puzzle_input:
	for line in puzzle_input.readlines():
		digits = ""
		for char in line:
			if char.isnumeric():
				digits += char
		sum_calibration_values += int(digits[0] + digits[-1])

print(sum_calibration_values)
