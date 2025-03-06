# URL:		https://adventofcode.com/2022/day/1#part2
# Answer:	198551

import os
from itertools import groupby
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day1_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2022\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2022/day1_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2022/day1_example.txt'

most_calories =  []

with open(puzzle_input, 'r') as data:
	food_items = [x.removesuffix("\n") for x in data.readlines()]
	items_per_elf = [list(group) for k, group in groupby(food_items, lambda x: x != '') if k]
	for elf in items_per_elf:
		most_calories.append(sum(list(map(int, elf))))

most_calories.sort(reverse=True)
top_three_elfes = sum(most_calories[0:3])
print(top_three_elfes)
