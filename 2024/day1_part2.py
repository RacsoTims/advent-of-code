# URL:		https://adventofcode.com/2024/day/1#part2
# Answer:	23981443

import os
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2024\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2024/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2024/day1_example.txt'

similarity_score = 0

with open(puzzle_input, 'r') as data:
	location_ids = (data.read()).split(None)

list_left = location_ids[::2]
list_right = location_ids[1::2]

for number in list_left:
    similarity_score += int(number) * list_right.count(number)
print(similarity_score)
