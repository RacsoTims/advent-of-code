# URL:		https://adventofcode.com/2021/day/4#part2
# Answer:	13912

import os
import numpy as np
puzzle_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day4_input.txt'
example_input = 'C:\\Users\\oscar\\my_stuff\\advent-of-code\\2021\\day4_example.txt'
if os.name == 'posix':
	puzzle_input = '/home/oscar/projects/advent-of-code/2021/day4_input.txt'
	example_input = '/home/oscar/projects/advent-of-code/2021/day4_example.txt'

draws = []
cards = []
results = {}

with open(puzzle_input, 'r') as data:
	i = 0
	for line in [(x.removeprefix(" ")).removesuffix("\n") for x in data.readlines()]:
		if "," in line:
			draws = list(map(int, line.split(",")))
		elif line == "":
			i += 1
			continue
		else:
			if i % 6 == 2:
				card = []
				row = row = line.replace("  ", " ").split(" ")
				card.append(row)
			else:
				row = line.replace("  ", " ").split(" ")
				card.append(row)
			if len(card) == 5:
				cards.append(np.array(card, dtype=int))
		i += 1

for bingo_card in cards:
    for j in range(len(draws)):
        number = draws[j]
        bingo_card[bingo_card == number] = -1
        if np.any(np.all(bingo_card == -1, axis=1)) or np.any(np.all(bingo_card == -1, axis=0)):
            sum_unmarked_numbers = np.sum(bingo_card) + np.count_nonzero(bingo_card == -1)
            score = sum_unmarked_numbers * number
            results[j+1] = score
            break

finish_last = max(results)
winner = list(results.keys()).index(finish_last) + 1
winning_score = results[finish_last]

print(f"Card {winner} was the last to finish by having bingo after {finish_last} draws.")
print(f"Their final score was: {winning_score}")
