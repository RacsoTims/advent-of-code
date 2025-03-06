# URL:		https://adventofcode.com/2018/day/1#part2
# Answer:	287

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2018\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2018\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2018/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2018/day1_example.txt'

frequency = 0
frequencies = []
frequency_reached_twice = False

while not frequency_reached_twice:
	with open(puzzle_input, 'r') as data:
		for x in data.readlines():
			change = int(x)
			frequency += change
			if frequency not in frequencies:
				frequencies.append(frequency)
			else:
				frequency_reached_twice = True
				break
print(frequency)
