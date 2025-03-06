# URL:		https://adventofcode.com/2021/day/1#part2
# Answer:	1653

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2021/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2021/day1_example.txt'

count = 0
window_size = 3

with open(puzzle_input, 'r') as data:
	measurements = [int(x) for x in data.readlines()]
	for i in range(0, len(measurements)-window_size):
		if (sum(measurements[i:i+window_size])) < sum(measurements[i+1:i+window_size+1]):
			count += 1

print(count)
