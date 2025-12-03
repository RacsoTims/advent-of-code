# URL:		https://adventofcode.com/2022/day/1
# Answer:	66719

from itertools import groupby
import os
puzzle_input = '.\\day1_input.txt'
example_input = '.\\day1_example.txt'
if os.name == 'posix':
	puzzle_input = './day1_input.txt'
	example_input = './day1_example.txt'

most_calories =  0

with open(puzzle_input, 'r') as data:
	food_items = [x.removesuffix("\n") for x in data.readlines()]
	items_per_elf = [list(group) for k, group in groupby(food_items, lambda x: x != '') if k]
	for elf in items_per_elf:
		calories = sum(list(map(int, elf)))
		if calories > most_calories:
			most_calories = calories
print(most_calories)
