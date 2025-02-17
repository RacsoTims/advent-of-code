# URL:      https://adventofcode.com/2021/day/4
# Answer:   72770

import numpy as np

path = "/home/oscar/projects/advent-of-code/2021/day4_input.txt"
draws = []
cards = []
results = {}

with open(path, 'r') as puzzle_input:
    i = 0
    for line in [(x.removeprefix(" ")).removesuffix("\n") for x in puzzle_input.readlines()]:
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

quickest_win = min(results)
winner = list(results.keys()).index(quickest_win) + 1
winning_score = results[quickest_win]

print(f"Card {winner} won the game by having bingo after {quickest_win} draws.")
print(f"Their final score was: {winning_score}")
