# URL:		https://adventofcode.com/2020/day/7
# Answer:	0

import os
import re
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day7_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2020\\day7_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2020/day7_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2020/day7_example.txt'

count = 0
regex_outer_bag = r'(.+)s contain'
regex_inner_bag = r'(\d+ [a-z ]+? bag)'
bag_system = {}

with open(example_input, 'r') as data:
	for rule in data.readlines():
		outer_bag = re.match(regex_outer_bag, rule).group(1)
		inner_bags = re.findall(regex_inner_bag, rule)
		bag_system[outer_bag] = {}
		for inner_bag in inner_bags:
			colour = re.match(r'\d+ (.+)', inner_bag).group(1)
			quantity = int(re.match(r'\d+', inner_bag).group(0))
			bag_system[outer_bag][colour] = quantity
print(bag_system)
print(count)
