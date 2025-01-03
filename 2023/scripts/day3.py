import re
from operator import mul

with open('C:/Users/Gebruiker/projects/powershell/advent-of-code/data/2023_day3_data.txt', 'r') as f:
    puzzle_input = f.read()

counter = 0
def part1(puzzle_input, counter):

    lines = puzzle_input.split('\n')

    symbol_regex = r'[^.\d]'
    symbol_adjacent = set()
    for i, line in enumerate(lines):
        for m in re.finditer(symbol_regex, line):
            j = m.start()
            symbol_adjacent |= {(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2)}

    number_regex = r'\d+'
    part_num_sum = 0
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            if any((i, j) in symbol_adjacent for j in range(*m.span())):
                with open('output.txt', 'a') as output:
                    output.write(f"{m.group()}\n")
                part_num_sum += int(m.group())
                counter += 1

    return part_num_sum, counter


def part2(puzzle_input):
    lines = puzzle_input.split('\n')

    gear_regex = r'\*'
    gears = dict()
    for i, line in enumerate(lines):
        for m in re.finditer(gear_regex, line):
            gears[(i, m.start())] = []

    number_regex = r'\d+'
    for i, line in enumerate(lines):
        for m in re.finditer(number_regex, line):
            for r in range(i-1, i+2):
                for c in range(m.start()-1, m.end()+1):
                    if (r, c) in gears:
                        gears[(r, c)].append(int(m.group()))

    gear_ratio_sum = 0
    for nums in gears.values():
        if len(nums) == 2:
            gear_ratio_sum += mul(*nums)

    return gear_ratio_sum



print('Part 1:', part1(puzzle_input, counter))
print('Part 2:', part2(puzzle_input))