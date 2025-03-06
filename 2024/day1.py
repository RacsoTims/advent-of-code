# URL:		https://adventofcode.com/2024/day/1
# Answer:	1258579

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2024/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2024/day1_example.txt'

total_distance = 0

with open(puzzle_input, 'r') as data:
	location_ids = (data.read()).split(None)

list_left = location_ids[::2]
list_right = location_ids[1::2]

list_left.sort()
list_right.sort()

for i in range(len(list_left)):
    total_distance += abs(int(list_left[i]) - int(list_right[i]))
print(total_distance)
