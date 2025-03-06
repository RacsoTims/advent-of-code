# URL:		https://adventofcode.com/2016/day/6
# Answer:	gyvwpxaz

import os
import numpy as np
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day6_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day6_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2016/day6_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2016/day6_example.txt'

corrected_message = ""

with open(puzzle_input, 'r') as data:
	list_of_lines = [x.removesuffix("\n") for x in data.readlines()]

grid = np.array([list(line) for line in list_of_lines])

for column in grid.T:
    unique_letters, counts = np.unique_counts(column)
    most_frequent_letter = unique_letters[np.argmax(counts)]
    corrected_message += most_frequent_letter
print(corrected_message)
