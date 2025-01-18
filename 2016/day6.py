# URL: https://adventofcode.com/2016/day/6
# Answer:   gyvwpxaz

import numpy as np

path = "C:\\Users\\oscar\\my_stuff\\advent-of-code\\2016\\day6_input.txt"
corrected_message = ""

with open(path, "r") as puzzle_input:
    list_of_lines = [x.removesuffix("\n") for x in puzzle_input.readlines()]

grid = np.array([list(line) for line in list_of_lines])

for column in grid.T:
    unique_letters, counts = np.unique_counts(column)
    most_frequent_letter = unique_letters[np.argmax(counts)]
    corrected_message += most_frequent_letter
print(corrected_message)
